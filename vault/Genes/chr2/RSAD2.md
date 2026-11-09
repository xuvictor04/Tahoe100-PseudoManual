---
symbol: "RSAD2"
type: "gene"
col: 5546
ensembl_id: "ENSG00000134321"
name: "radical S-adenosyl methionine domain containing 2"
location: "2p25.2"
module: 32
arm: "+"
pooled_cpm: 56.35
n_lines_expressing: 36
n_dd_up: 35
n_dd_down: 67
n_dd_up_clean: 35
n_dd_down_clean: 58
in_vector_space: true
direction_upstream: 53
direction_downstream: 114
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# RSAD2

*radical S-adenosyl methionine domain containing 2* — 2p25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 5.29× (z +12.5, q 3e-33, up in 31 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 67 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.153× (z -14.1, q 3e-42, down in 33 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFIT3]] (+0.95, fdr 7e-06), [[XAF1]] (+0.94, fdr 7e-06), [[IFI44]] (+0.93, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 53 arrows point to it, the strongest [[SAMD9L]] → it (grade B ⚠); 114 go from it, the strongest it → [[SP100]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, none with an alert; shown: the 15 strongest. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5546.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **5.29×** | +12.5 | 3e-33 | 31/34 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.52×** | +9.5 | 8e-19 | 25/34 (NCI-H460, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **3.25×** | +8.5 | 3e-15 | 18/34 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **3.09×** | +8.2 | 5e-14 | 28/33 (RKO, AsPC-1, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **2.11×** | +5.4 | 6e-06 | 23/34 (RKO, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.85×** | +5.1 | 3e-05 | 22/35 (RKO, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.70×** | +5.0 | 5e-05 | 22/35 (HEC-1-A, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.93×** | +5.0 | 5e-05 | 21/35 (RKO, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.70×** | +4.9 | 6e-05 | 18/34 (RKO, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.66×** | +4.9 | 6e-05 | 20/34 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.90×** | +4.8 | 7e-05 | 15/34 (NCI-H460, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 5 µM |  | **1.54×** | +4.6 | 2e-04 | 19/34 (NCI-H2347, NCI-H1792, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.50×** | +4.2 | 9e-04 | 19/34 (CFPAC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.79×** | +4.2 | 9e-04 | 23/34 (SK-MEL-2, KATO III, …) | top dose only |  |
| [[venetoclax (drug)]] 0.05 µM |  | **1.79×** | +4.2 | 0.001 | 18/35 (LoVo, RKO, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 67 in all, 9 with an alert ⚠; shown: the 15 strongest. 67 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5546.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.153×** | -14.1 | 3e-42 | 33/34 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.165×** | -13.5 | 3e-39 | 33/34 (A-172, RKO, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.315×** | -12.2 | 3e-32 | 27/34 (HS-578T, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.225×** | -11.2 | 5e-27 | 30/34 (A-172, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.257×** | -10.2 | 3e-22 | 27/35 (MIA PaCa-2, HS-578T, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.259×** | -10.1 | 4e-22 | 29/34 (MIA PaCa-2, BT-474, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.392×** | -9.9 | 3e-21 | 26/35 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.424×** | -9.1 | 7e-18 | 24/35 (NCI-H2347, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.304×** | -8.9 | 2e-17 | 27/34 (BT-474, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.308×** | -8.8 | 6e-17 | 24/35 (MIA PaCa-2, BT-474, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.360×** | -7.7 | 1e-12 | 25/34 (LoVo, SNU-423, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.374×** | -7.4 | 8e-12 | 27/34 (SNU-423, A-172, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.543×** | -6.5 | 5e-09 | 24/35 (A-172, MIA PaCa-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.557×** | -6.2 | 2e-08 | 22/34 (NCI-H1792, Panc 03.27, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.438×** | -6.2 | 2e-08 | 22/34 (A549, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~15% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5546. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 533 | 0 | 17 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0245× (z -21.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0267× (z -21.2) |
| [[CFPAC-1 (line)]] | alt | 171 | 1 | 13 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 6.73× (z +9.3) | [[Tofacitinib (drug)]] 5 µM 0.108× (z -15.9) |
| [[BT-474 (line)]] | alt | 43.4 | 0 | 13 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0300× (z -13.1) |
| [[MIA PaCa-2 (line)]] | alt | 74.3 | 1 | 12 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 8.15× (z +8.5) | [[Tofacitinib (drug)]] 5 µM 0.0712× (z -14.9) |
| [[SNU-423 (line)]] | alt | 55.6 | 0 | 13 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0262× (z -15.0) |
| [[HS-578T (line)]] | alt | 75.3 | 2 | 9 (3 ⚠) | [[Harringtonine (drug)]] 0.5 µM 15.6× (z +10.8) | [[Selinexor (drug)]] 5 µM 0.0820× (z -13.9) |
| [[LoVo (line)]] | wt | 85.6 | 0 | 11 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.145× (z -12.6) |
| [[NCI-H2347 (line)]] | alt | 59.5 | 3 | 8 | [[Harringtonine (drug)]] 0.5 µM 8.07× (z +11.1) | [[Tofacitinib (drug)]] 5 µM 0.131× (z -15.2) |
| [[RPMI-7951 (line)]] | alt | 125 | 0 | 9 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0465× (z -14.1) |
| [[NCI-H1792 (line)]] | alt | 37.8 | 0 | 8 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.0879× (z -12.5) |
| [[NCI-H460 (line)]] | wt | 117 | 6 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 7.85× (z +17.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 13.6× (z +15.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -9.6) |
| [[A549 (line)]] | wt | 27.5 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0918× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.127× (z -11.6) |
| [[COLO 205 (line)]] | alt | 164 | 0 | 6 | — | [[Selinexor (drug)]] 5 µM 0.0473× (z -12.3) |
| [[H4 (line)]] | wt | 59.7 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -10.6) |
| [[KATO III (line)]] | alt | 54.7 | 0 | 3 | — | [[Tofacitinib (citrate) (drug)]] 5 µM 0.0984× (z -11.4) |
| [[Panc 03.27 (line)]] | alt | 129 | 0 | 3 | — | [[Tofacitinib (drug)]] 5 µM 0.241× (z -8.8) |
| [[RKO (line)]] | wt | 30.0 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.00798× (z -16.1) |
| [[SK-MEL-2 (line)]] | alt | 28.1 | 2 | 1 | [[Harringtonine (drug)]] 0.5 µM 11.1× (z +9.1) | [[Tofacitinib (drug)]] 5 µM 0.190× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 32.5 | 1 | 1 | [[Harringtonine (drug)]] 0.5 µM 4.41× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.184× (z -9.8) |
| [[LS 180 (line)]] | wt | 41.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.44× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 16.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 47.1× (z +13.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 64.2× (z +10.4) | — |
| [[A498 (line)]] | wt | 32.3 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.205× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 22.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.57× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HepG2_C3A (line)]] | wt | 28.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0263× (z -10.6) |
| [[Hs 766T (line)]] | wt | 101 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -8.6) |
| [[HT-29 (line)]] | alt | 19.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.46× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H1573 (line)]] | alt | 21.3 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.113× (z -12.5) |
| [[SHP-77 (line)]] | alt | 31.8 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0428× (z -9.4) |
| [[SW 900 (line)]] | alt | 56.6 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 9.21× (z +8.5) | — |
| [[A-427 (line)]] | wt | 4.01 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.28 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 14.0 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.69 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.67 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.29 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 8.32 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.48 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.61 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.50 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.03 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.87 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.98 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.63 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5546), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFIT3]] | +0.95 | +0.92 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 999 |
| [[XAF1]] | +0.94 | +0.88 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 900 |
| [[IFI44]] | +0.93 | +0.91 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 983 |
| [[IFIT1]] | +0.93 | +0.89 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 970 |
| [[CMPK2]] | +0.92 | +0.88 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 976; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[MX2]] | +0.92 | +0.87 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 963 |
| [[MX1]] | +0.92 | +0.88 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 983 |
| [[PARP9]] | +0.91 | +0.84 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 866 |
| [[PARP14]] | +0.91 | +0.86 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 751 |
| [[HERC6]] | +0.91 | +0.87 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 903 |
| [[OAS2]] | +0.91 | +0.85 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 950 |
| [[OAS1]] | +0.91 | +0.85 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 967 |
| [[IFIH1]] | +0.91 | +0.86 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 954 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*53 arrows, 53 of them with an alert ⚠; grade A 0, B 42, C 11. Shown: the 12 strongest; 41 more arrows (41 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAMD9L]] | B | SAMD9L activity raises RSAD2's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 3.84× lower at baseline in the lines without SAMD9L | 0.001 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[GBP4]] | B | GBP4 activity raises RSAD2's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 3.50× lower at baseline in the lines without GBP4 | 0.001 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[OAS2]] | B | OAS2 activity raises RSAD2's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 4.11× lower at baseline in the lines without OAS2 | 0.002 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[EPSTI1]] | B | EPSTI1 activity raises RSAD2's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 3.74× lower at baseline in the lines without EPSTI1 | 0.002 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[NRIR]] | B | NRIR activity raises RSAD2's level | lines that do not express NRIR (14) vs lines expressing it (36) | 4.13× lower at baseline in the lines without NRIR | 0.004 | ⚠ within organs, on part of the lines; also absent: CMPK2, TSPAN7 |
| [[IFIT3]] | B | IFIT3 activity raises RSAD2's level | lines that do not express IFIT3 (8) vs lines expressing it (42) | 4.07× lower at baseline in the lines without IFIT3 | 0.006 | ⚠ within organs, on part of the lines; also absent: GBP2, IFIT2, TRIM38; maybe low, not absent |
| [[TRIM22]] | B | TRIM22 activity raises RSAD2's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 3.46× lower at baseline in the lines without TRIM22 | 0.006 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[SAMD9]] | B | SAMD9 activity raises RSAD2's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 3.60× lower at baseline in the lines without SAMD9 | 0.006 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[NLRC5]] | B | NLRC5 activity raises RSAD2's level | lines that do not express NLRC5 (5) vs lines expressing it (45) | 5.56× lower at baseline in the lines without NLRC5 | 0.007 | ⚠ within organs, on part of the lines; also absent: NDRG1, APOL6, S100A13; maybe low, not absent |
| [[APOL6]] | B | APOL6 activity raises RSAD2's level | lines that do not express APOL6 (6) vs lines expressing it (44) | 4.50× lower at baseline in the lines without APOL6 | 0.007 | ⚠ within organs, on part of the lines; also absent: KLF4, S100A13, LGALS3BP; maybe low, not absent |
| [[HERC6]] | B | HERC6 activity raises RSAD2's level | lines that do not express HERC6 (5) vs lines expressing it (45) | 5.55× lower at baseline in the lines without HERC6 | 0.008 | ⚠ within organs, on part of the lines; also absent: IFIH1, IFI35, PARP9; maybe low, not absent |
| [[APOL3]] | B | APOL3 activity raises RSAD2's level | lines that do not express APOL3 (14) vs lines expressing it (36) | 3.41× lower at baseline in the lines without APOL3 | 0.010 | ⚠ within organs, on part of the lines; also absent: SAMD9L, APOL1, GBP4 |

### Downstream of this gene

*114 arrows, 114 of them with an alert ⚠; grade A 0, B 104, C 10. Shown: the 12 strongest; 102 more arrows (102 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SP100]] | B | RSAD2 activity raises SP100's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 2.61× lower at baseline in the lines without RSAD2 | 3e-04 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[NLRC5]] | B | RSAD2 activity raises NLRC5's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 2.59× lower at baseline in the lines without RSAD2 | 8e-04 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[IFIT3]] | B | RSAD2 activity raises IFIT3's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 3.38× lower at baseline in the lines without RSAD2 | 0.001 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[DDX60]] | B | RSAD2 activity raises DDX60's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 3.21× lower at baseline in the lines without RSAD2 | 0.001 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[SAMD9]] | B | RSAD2 activity raises SAMD9's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 3.59× lower at baseline in the lines without RSAD2 | 0.001 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[DDX60L]] | B | RSAD2 activity raises DDX60L's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 3.03× lower at baseline in the lines without RSAD2 | 0.001 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[HERC6]] | B | RSAD2 activity raises HERC6's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 2.61× lower at baseline in the lines without RSAD2 | 0.001 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[CMPK2]] | B | RSAD2 activity raises CMPK2's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 3.45× lower at baseline in the lines without RSAD2 | 0.001 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[PARP14]] | B | RSAD2 activity raises PARP14's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 2.38× lower at baseline in the lines without RSAD2 | 0.001 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[APOL6]] | B | RSAD2 activity raises APOL6's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 2.97× lower at baseline in the lines without RSAD2 | 0.001 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[TRANK1]] | B | RSAD2 activity raises TRANK1's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 2.89× lower at baseline in the lines without RSAD2 | 0.002 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[OAS2]] | B | RSAD2 activity raises OAS2's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 3.91× lower at baseline in the lines without RSAD2 | 0.002 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.952). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.2, 53.5); signed map (64.5, 31.4). **Vector** length 157, 56.9% of its response variance represented; |z| ≥ 3 in 1,478 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interferon gamma signaling* (reactome, mean cos +0.77 to 17); *Antimicrobial mechanism of IFN-stimulated genes* (reactome, mean cos +0.85 to 21); *Modulation of host responses by IFN-stimulated genes* (reactome, mean cos +0.83 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +10.7 | +12.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.4 | +9.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.2 | +8.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.9 | +8.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.8 | +0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.6 | +4.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.2 | +4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.1 | +5.4 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -9.2 | -9.9 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -7.9 | -9.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -7.8 | -8.8 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -7.5 | -7.7 |
|  | [[Selinexor (drug)]] 5 µM |  | -7.2 | -12.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -6.1 | -10.2 |

## What is on record

|  |  |
|---|---|
| Name | radical S-adenosyl methionine domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.2 — chr2:6,865,557-6,898,239 (+) |
| Ensembl biotype | protein_coding |
| Also known as | cig5, vig1, Viperin |
| Gene groups (HGNC) | Radical S-adenosylmethionine domain containing; Carbon-oxygen lyases |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, KRAS_SIGNALING_DN, INTERFERON_GAMMA_RESPONSE |
| Reactome | 3 pathways, smallest: Interferon alpha/beta signaling; Interferon Signaling; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WXG1](https://www.uniprot.org/uniprotkb/Q8WXG1) (S-adenosylmethionine-dependent nucleotide dehydratase RSAD2):

> Interferon-inducible antiviral protein which plays a major role in the cell antiviral state induced by type I and type II interferon. Catalyzes the conversion of cytidine triphosphate (CTP) to 3'-deoxy-3',4'-didehydro-CTP (ddhCTP) via a SAM-dependent radical mechanism. In turn, ddhCTP acts as a chain terminator for the RNA-dependent RNA polymerases from multiple viruses and directly inhibits viral replication. Therefore, inhibits a wide range of DNA and RNA viruses, including human …

**Summary**, from NCBI Gene [91543](https://www.ncbi.nlm.nih.gov/gene/91543):

> The protein encoded by this gene is an interferon-inducible antiviral protein that belongs to the S-adenosyl-L-methionine (SAM) superfamily of enzymes. The protein plays a role in cellular antiviral response and innate immune signaling. Antiviral effects result from inhibition of viral RNA replication, interference in the secretory pathway, binding to viral proteins and dysregulation of cellular lipid metabolism. The protein has been found to inhibit both DNA and RNA viruses, including …

**Accessions** — [HGNC:30908](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30908) · Entrez [91543](https://www.ncbi.nlm.nih.gov/gene/91543) · UniProt [Q8WXG1](https://www.uniprot.org/uniprotkb/Q8WXG1) · Ensembl [ENSG00000134321](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134321)

## Data

Gene col 5546: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5546); `tables/drug_effects.parquet` (102 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5546, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5546]; `tensor/DDL_lfc|DDL_z.npy` [5546]; `embed/gene_vectors.npy` [5546]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5546 or target_col == 5546). Every well: [[RSAD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RSAD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
