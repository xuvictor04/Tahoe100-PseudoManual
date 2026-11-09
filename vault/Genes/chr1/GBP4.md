---
symbol: "GBP4"
type: "gene"
col: 8556
ensembl_id: "ENSG00000162654"
name: "guanylate binding protein 4"
location: "1p22.2"
module: 70
arm: "+"
pooled_cpm: 21.68
n_lines_expressing: 30
n_dd_up: 27
n_dd_down: 60
n_dd_up_clean: 24
n_dd_down_clean: 54
in_vector_space: true
direction_upstream: 63
direction_downstream: 131
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# GBP4

*guanylate binding protein 4* — 1p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 2.85× (z +9.8, q 6e-20, up in 24 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 60 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.175× (z -16.4, q 0e+00, down in 27 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRANK1]] (+0.85, fdr 7e-06), [[APOL3]] (+0.85, fdr 7e-06), [[PSMB9]] (+0.84, fdr 7e-06).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 63 arrows point to it, the strongest [[CTSS]] → it (grade B ⚠); 131 go from it, the strongest it → [[DDX60]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8556.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **2.85×** | +9.8 | 6e-20 | 24/28 (NCI-H2347, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **2.38×** | +7.9 | 8e-13 | 22/27 (CFPAC-1, Hs 766T, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **2.01×** | +7.0 | 5e-10 | 21/28 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.81×** | +6.7 | 3e-09 | 24/28 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.90×** | +5.9 | 5e-07 | 20/27 (Hs 766T, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.64×** | +5.7 | 1e-06 | 18/28 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.64×** | +5.6 | 2e-06 | 16/28 (CFPAC-1, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.80×** | +5.5 | 3e-06 | 19/28 (CFPAC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.62×** | +4.6 | 3e-04 | 15/27 (NCI-H1792, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.62×** | +4.6 | 3e-04 | 13/25 (Hs 766T, NCI-H1792, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.68×** | +4.1 | 0.002 | 14/28 (CFPAC-1, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.79×** | +3.9 | 0.004 | 13/28 (Hs 766T, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.35×** | +3.8 | 0.005 | 12/28 (CFPAC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.35×** | +3.8 | 0.006 | 12/28 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.010 | 9/27 (NCI-H1792, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.50×** | +3.6 | 0.013 | 14/28 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 60 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 60 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8556.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.175×** | -16.4 | 0e+00 | 27/28 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.206×** | -14.8 | 0e+00 | 26/28 (A498, COLO 205, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.211×** | -14.6 | 0e+00 | 28/28 (A498, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.255×** | -12.8 | 1e-35 | 26/28 (Panc 03.27, A498, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.415×** | -11.7 | 2e-29 | 25/28 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.293×** | -11.5 | 8e-29 | 26/28 (NCI-H2347, A498, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.314×** | -10.9 | 1e-25 | 22/28 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.464×** | -10.2 | 2e-22 | 22/28 (A549, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.496×** | -9.3 | 9e-19 | 18/28 (A498, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.390×** | -8.8 | 5e-17 | 25/28 (A498, NCI-H1792, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.374×** | -8.5 | 7e-16 | 15/22 (A-172, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.417×** | -8.2 | 1e-14 | 25/28 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.423×** | -8.1 | 3e-14 | 24/28 (A-172, CFPAC-1, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.425×** | -8.0 | 4e-14 | 21/28 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.560×** | -7.7 | 7e-13 | 25/28 (SK-MEL-2, A-172, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.452×** | -7.4 | 4e-12 | 21/28 (NCI-H2347, A498, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.463×** | -7.2 | 2e-11 | 20/28 (BT-474, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.467×** | -7.1 | 3e-11 | 20/28 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8556. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 66.6 | 0 | 21 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0546× (z -22.7) |
| [[NCI-H2347 (line)]] | alt | 24.3 | 1 | 16 (4 ⚠) | [[Harringtonine (drug)]] 0.5 µM 6.77× (z +11.3) | [[Tofacitinib (drug)]] 5 µM 0.204× (z -13.4) |
| [[A549 (line)]] | wt | 21.2 | 0 | 14 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0732× (z -17.5) |
| [[CFPAC-1 (line)]] | alt | 143 | 1 | 11 (2 ⚠) | [[Cobimetinib (drug)]] 5 µM 3.73× (z +8.8) | [[Tofacitinib (drug)]] 5 µM 0.186× (z -16.4) |
| [[SNU-423 (line)]] | alt | 33.2 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -15.3) |
| [[A-172 (line)]] | wt | 22.5 | 0 | 11 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0505× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0680× (z -14.8) |
| [[NCI-H1792 (line)]] | alt | 40.3 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0931× (z -20.9) |
| [[HS-578T (line)]] | alt | 62.7 | 1 | 6 (3 ⚠) | [[Harringtonine (drug)]] 0.5 µM 6.22× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.0178× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.116× (z -14.5) |
| [[SK-MEL-2 (line)]] | alt | 36.9 | 0 | 7 | — | [[Panobinostat (drug)]] 0.5 µM 0.0784× (z -13.9) |
| [[NCI-H1573 (line)]] | alt | 16.7 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0482× (z -11.7) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.127× (z -11.2) |
| [[CHP-212 (line)]] | wt | 18.5 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0207× (z -11.1) |
| [[RPMI-7951 (line)]] | alt | 21.3 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0316× (z -15.5) |
| [[BT-474 (line)]] | alt | 14.9 | 0 | 4 | — | [[Selinexor (drug)]] 5 µM 0.0837× (z -12.6) |
| [[J82 (line)]] | alt | 25.2 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 8.02× (z +9.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.47× (z +8.9) | — |
| [[Panc 03.27 (line)]] | alt | 74.0 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0733× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.147× (z -12.4) |
| [[COLO 205 (line)]] | alt | 12.7 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.0407× (z -11.7) |
| [[LoVo (line)]] | wt | 8.88 | 0 | 3 | — | [[Selinexor (drug)]] 5 µM 0.201× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 57.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.53× (z +13.2) | [[Panobinostat (drug)]] 5 µM 0.147× (z -9.4) |
| [[PANC-1 (line)]] | alt | 22.8 | 1 | 1 | [[Harringtonine (drug)]] 0.5 µM 6.90× (z +10.7) | [[Ixazomib citrate (drug)]] 5 µM 0.205× (z -8.8) |
| [[C32 (line)]] | wt | 8.19 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0806× (z -8.9) ⚠ toxic |
| [[H4 (line)]] | wt | 13.5 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0547× (z -9.4) |
| [[Hs 766T (line)]] | wt | 94.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.163× (z -9.4) |
| [[KATO III (line)]] | alt | 8.52 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -9.7) |
| [[SW 900 (line)]] | alt | 15.5 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.121× (z -9.1) |
| [[A-427 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.53 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.53 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.28 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.00 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.19 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.94 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.51 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8556), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRANK1]] | +0.85 | +0.78 / +0.87 | both halves | 7e-06 |  |
| [[APOL3]] | +0.85 | +0.82 / +0.83 | both halves | 7e-06 | STRING 485 |
| [[PSMB9]] | +0.84 | +0.83 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 497 |
| [[GBP1]] | +0.84 | +0.81 / +0.83 | both halves | 7e-06 | same gene group; pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 905 |
| [[EPSTI1]] | +0.84 | +0.76 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 767 |
| [[SAMD9L]] | +0.83 | +0.77 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 650 |
| [[SLC15A3]] | +0.83 | +0.80 / +0.83 | both halves | 7e-06 |  |
| [[HERC5]] | +0.83 | +0.74 / +0.87 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 525 |
| [[XAF1]] | +0.82 | +0.75 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 633 |
| [[OAS1]] | +0.82 | +0.73 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 520 |
| [[PARP14]] | +0.81 | +0.70 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 751 |
| [[GBP3]] | +0.81 | +0.75 / +0.82 | both halves | 7e-06 | same gene group; pathway: Antimicrobial mechanism of IFN-stimulated genes |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*63 arrows, 63 of them with an alert ⚠; grade A 0, B 33, C 30. Shown: the 12 strongest; 51 more arrows (51 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTSS]] | B | CTSS activity raises GBP4's level | lines that do not express CTSS (15) vs lines expressing it (35) | 3.56× lower at baseline in the lines without CTSS | 0.001 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[CD74]] | B | CD74 activity raises GBP4's level | lines that do not express CD74 (31) vs lines expressing it (19) | 2.28× lower at baseline in the lines without CD74 | 0.004 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, SHROOM4, LAPTM5 |
| [[MX1]] | B | MX1 activity raises GBP4's level | lines that do not express MX1 (19) vs lines expressing it (31) | 2.78× lower at baseline in the lines without MX1 | 0.005 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[IL15]] | B | IL15 activity raises GBP4's level | lines that do not express IL15 (10) vs lines expressing it (40) | 4.52× lower at baseline in the lines without IL15 | 0.006 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[LGALS9]] | B | LGALS9 activity raises GBP4's level | lines that do not express LGALS9 (13) vs lines expressing it (37) | 2.77× lower at baseline in the lines without LGALS9 | 0.008 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ATP8B1, CTSS; maybe low, not absent |
| [[IFI44]] | B | IFI44 activity raises GBP4's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 3.89× lower at baseline in the lines without IFI44 | 0.008 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[UBA7]] | B | UBA7 activity raises GBP4's level | lines that do not express UBA7 (9) vs lines expressing it (41) | 4.36× lower at baseline in the lines without UBA7 | 0.010 | ⚠ within organs, on part of the lines; also absent: XAF1, SH3TC1, SLC15A3; maybe low, not absent |
| [[CYP2J2]] | B | CYP2J2 activity raises GBP4's level | lines that do not express CYP2J2 (12) vs lines expressing it (38) | 3.01× lower at baseline in the lines without CYP2J2 | 0.013 | ⚠ within organs, on part of the lines; also absent: CDK18 |
| [[IFIT2]] | B | IFIT2 activity raises GBP4's level | lines that do not express IFIT2 (8) vs lines expressing it (42) | 5.16× lower at baseline in the lines without IFIT2 | 0.014 | ⚠ within organs, on part of the lines; also absent: IFIT3, ENSG00000235609, TRIM38 |
| [[NEURL3]] | B | NEURL3 activity raises GBP4's level | lines that do not express NEURL3 (13) vs lines expressing it (37) | 3.33× lower at baseline in the lines without NEURL3 | 0.017 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA4, VSIR; maybe low, not absent |
| [[LINC01285]] | B | LINC01285 activity raises GBP4's level | lines that do not express LINC01285 (21) vs lines expressing it (29) | 1.86× lower at baseline in the lines without LINC01285 | 0.022 | ⚠ within organs, on part of the lines; also absent: HNF1A, SLC22A3, LINC01819; maybe low, not absent |
| [[CASP10]] | B | CASP10 activity raises GBP4's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 2.56× lower at baseline in the lines without CASP10 | 0.024 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |

### Downstream of this gene

*131 arrows, 131 of them with an alert ⚠; grade A 0, B 104, C 27. Shown: the 12 strongest; 119 more arrows (119 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DDX60]] | B | GBP4 activity raises DDX60's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 3.20× lower at baseline in the lines without GBP4 | 6e-04 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[NLRC5]] | B | GBP4 activity raises NLRC5's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 2.00× lower at baseline in the lines without GBP4 | 1e-03 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[NRIR]] | B | GBP4 activity raises NRIR's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 2.12× lower at baseline in the lines without GBP4 | 0.001 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[DDX60L]] | B | GBP4 activity raises DDX60L's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 3.58× lower at baseline in the lines without GBP4 | 0.001 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[PARP14]] | B | GBP4 activity raises PARP14's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 2.33× lower at baseline in the lines without GBP4 | 0.001 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[APOL6]] | B | GBP4 activity raises APOL6's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 2.55× lower at baseline in the lines without GBP4 | 0.001 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[RSAD2]] | B | GBP4 activity raises RSAD2's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 3.50× lower at baseline in the lines without GBP4 | 0.001 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[OAS1]] | B | GBP4 activity raises OAS1's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 2.90× lower at baseline in the lines without GBP4 | 0.002 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[UBA7]] | B | GBP4 activity raises UBA7's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 2.44× lower at baseline in the lines without GBP4 | 0.002 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[IFIT3]] | B | GBP4 activity raises IFIT3's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 3.54× lower at baseline in the lines without GBP4 | 0.002 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[CMPK2]] | B | GBP4 activity raises CMPK2's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 2.59× lower at baseline in the lines without GBP4 | 0.002 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[HLA-B]] | B | GBP4 activity raises HLA-B's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 3.88× lower at baseline in the lines without GBP4 | 0.003 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.930). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.5, 51.7); signed map (62.3, 29.7). **Vector** length 153, 52.9% of its response variance represented; |z| ≥ 3 in 1,330 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Antigen processing-Cross presentation* (reactome, mean cos +0.70 to 14); *Endosomal/Vacuolar pathway* (reactome, mean cos +0.67 to 8); *ER-Phagosome pathway* (reactome, mean cos +0.70 to 13).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +6.6 | +9.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +6.1 | +7.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.0 | +7.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +4.8 | +5.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +3.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.8 | +6.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.5 | +5.9 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -7.1 | -11.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -6.5 | -11.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.2 | -12.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -6.0 | -10.9 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -6.0 | -8.0 |

## What is on record

|  |  |
|---|---|
| Name | guanylate binding protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.2 — chr1:89,181,144-89,198,942 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Mpa2 |
| Gene groups (HGNC) | Guanylate binding proteins |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, IL2_STAT5_SIGNALING, INTERFERON_GAMMA_RESPONSE |
| Reactome | 11 pathways, smallest: CASP4 inflammasome assembly; Enterobacterial factors antagonize host defense; GBP-mediated host defense |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96PP9](https://www.uniprot.org/uniprotkb/Q96PP9) (Guanylate-binding protein 4):

> Interferon (IFN)-inducible GTPase that plays important roles in innate immunity against a diverse range of bacterial, viral and protozoan pathogens (By similarity). Negatively regulates the antiviral response by inhibiting activation of IRF7 transcription factor (By similarity).

**Summary**, from NCBI Gene [115361](https://www.ncbi.nlm.nih.gov/gene/115361):

> Guanylate-binding proteins, such as GBP4, are induced by interferon and hydrolyze GTP to both GDP and GMP (Vestal, 2005 [PubMed 16108726]).[supplied by OMIM, Dec 2008]

**Accessions** — [HGNC:20480](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20480) · Entrez [115361](https://www.ncbi.nlm.nih.gov/gene/115361) · UniProt [Q96PP9](https://www.uniprot.org/uniprotkb/Q96PP9) · Ensembl [ENSG00000162654](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162654)

## Data

Gene col 8556: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8556); `tables/drug_effects.parquet` (87 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8556, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8556]; `tensor/DDL_lfc|DDL_z.npy` [8556]; `embed/gene_vectors.npy` [8556]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8556 or target_col == 8556). Every well: [[GBP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GBP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
