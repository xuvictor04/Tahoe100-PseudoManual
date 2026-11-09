---
symbol: "TRIM22"
type: "gene"
col: 5290
ensembl_id: "ENSG00000132274"
name: "tripartite motif containing 22"
location: "11p15.4"
module: 32
arm: "+"
pooled_cpm: 32.92
n_lines_expressing: 32
n_dd_up: 27
n_dd_down: 54
n_dd_up_clean: 23
n_dd_down_clean: 40
in_vector_space: true
direction_upstream: 44
direction_downstream: 120
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# TRIM22

*tripartite motif containing 22* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (4 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 2.77× (z +10.0, q 1e-20, up in 26 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 54 drug-doses (14 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.118× (z -21.7, q 0e+00, down in 30 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC15A3]] (+0.91, fdr 7e-06), [[EPSTI1]] (+0.91, fdr 7e-06), [[OAS2]] (+0.88, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 44 arrows point to it, the strongest [[LMO2]] → it (grade B ⚠); 120 go from it, the strongest it → [[HERC6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5290.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **2.77×** | +10.0 | 1e-20 | 26/29 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **2.19×** | +7.7 | 4e-12 | 26/29 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **2.03×** | +7.2 | 1e-10 | 24/29 (Hs 766T, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.70×** | +6.8 | 2e-09 | 24/30 (CFPAC-1, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.92×** | +6.7 | 3e-09 | 26/30 (A498, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.70×** | +6.5 | 5e-09 | 25/30 (AsPC-1, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.94×** | +6.4 | 9e-09 | 26/30 (CFPAC-1, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.71×** | +6.0 | 1e-07 | 26/30 (CFPAC-1, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.78×** | +5.9 | 3e-07 | 18/30 (NCI-H2347, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.52×** | +5.9 | 3e-07 | 20/30 (CFPAC-1, Hs 766T, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.50×** | +5.8 | 4e-07 | 23/30 (CFPAC-1, Hs 766T, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.75×** | +5.7 | 5e-07 | 26/30 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.72×** | +5.5 | 2e-06 | 21/30 (H4, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.42×** | +5.0 | 2e-05 | 15/30 (A498, LS 180, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 0.05 µM |  | **1.66×** | +4.9 | 3e-05 | 20/30 (LoVo, NCI-H2347, …) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.64×** | +4.8 | 7e-05 | 20/30 (Hs 766T, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 54 in all, 14 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 54 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5290.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.118×** | -21.7 | 0e+00 | 30/30 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.141×** | -19.9 | 0e+00 | 30/30 (A498, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.147×** | -19.5 | 0e+00 | 30/30 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.325×** | -16.2 | 0e+00 | 26/30 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.260×** | -13.7 | 1e-40 | 28/30 (HS-578T, SNU-423, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.260×** | -13.7 | 1e-40 | 29/30 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.266×** | -13.4 | 3e-39 | 25/30 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.394×** | -13.4 | 5e-39 | 25/30 (CFPAC-1, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.286×** | -12.7 | 3e-35 | 28/30 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.296×** | -12.4 | 2e-33 | 26/30 (BT-474, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.452×** | -11.4 | 3e-28 | 21/30 (NCI-H1792, SNU-423, …) | top dose only | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.340×** | -10.5 | 3e-24 | 22/28 (SNU-423, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.390×** | -9.6 | 5e-20 | 27/30 (MIA PaCa-2, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.372×** | -9.5 | 1e-19 | 27/30 (COLO 205, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.407×** | -9.1 | 3e-18 | 25/30 (A498, HS-578T, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.578×** | -7.9 | 1e-13 | 28/30 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.241×** | -6.9 | 2e-10 | 22/30 (A-172, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5290. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 35.0 | 0 | 23 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0316× (z -21.3) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Tofacitinib (drug)]] 0.5 µM 0.0327× (z -14.9) |
| [[SNU-423 (line)]] | alt | 106 | 0 | 22 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0640× (z -22.4) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0226× (z -21.8) |
| [[HS-578T (line)]] | alt | 85.6 | 2 (1 ⚠) | 18 (6 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.26× (z +8.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 3.23× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.0406× (z -23.9) |
| [[MIA PaCa-2 (line)]] | alt | 47.5 | 0 | 20 (7 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0183× (z -19.4) |
| [[A498 (line)]] | wt | 146 | 0 | 19 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0458× (z -27.3) |
| [[A-172 (line)]] | wt | 153 | 1 | 17 (5 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 2.99× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.0330× (z -29.8) |
| [[NCI-H1792 (line)]] | alt | 47.2 | 0 | 18 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0405× (z -22.5) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0191× (z -19.7) |
| [[RPMI-7951 (line)]] | alt | 99.2 | 0 | 18 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0339× (z -23.7) |
| [[NCI-H2347 (line)]] | alt | 85.3 | 1 | 16 (5 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.33× (z +9.8) | [[Panobinostat (drug)]] 0.5 µM 0.0780× (z -20.7) |
| [[CFPAC-1 (line)]] | alt | 52.9 | 1 | 14 (3 ⚠) | [[Cobimetinib (drug)]] 5 µM 3.76× (z +9.4) | [[Tofacitinib (drug)]] 5 µM 0.140× (z -20.3) |
| [[COLO 205 (line)]] | alt | 86.1 | 0 | 14 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0230× (z -17.7) |
| [[A549 (line)]] | wt | 34.1 | 0 | 13 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0660× (z -18.0) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0317× (z -16.1) |
| [[LoVo (line)]] | wt | 22.5 | 0 | 13 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0310× (z -17.8) |
| [[H4 (line)]] | wt | 90.0 | 1 | 6 (1 ⚠) | [[Selinexor (drug)]] 5 µM 3.05× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.0402× (z -18.4) |
| [[Hs 766T (line)]] | wt | 45.0 | 1 | 6 | [[Cobimetinib (drug)]] 5 µM 4.67× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.121× (z -12.8) |
| [[Panc 03.27 (line)]] | alt | 31.6 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.142× (z -10.6) |
| [[J82 (line)]] | alt | 38.3 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 5.44× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Tofacitinib (drug)]] 5 µM 0.331× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 15.1 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0536× (z -11.9) |
| [[AsPC-1 (line)]] | alt | 14.7 | 1 | 2 | [[Cobimetinib (drug)]] 5 µM 10.3× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.0996× (z -9.3) |
| [[hTERT-HPNE (line)]] | wt | 47.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.150× (z -10.3) |
| [[KATO III (line)]] | alt | 9.39 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -11.7) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0477× (z -11.5) |
| [[LS 180 (line)]] | wt | 12.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.136× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 24.2 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.101× (z -9.5) |
| [[RKO (line)]] | wt | 9.70 | 0 | 2 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0631× (z -8.6) |
| [[SW1417 (line)]] | alt | 10.9 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0422× (z -11.4) |
| [[SW 900 (line)]] | alt | 16.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.112× (z -10.6) |
| [[A-427 (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.82 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.49 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.38 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.84 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.13 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.03 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.82 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 5.59 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.00 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.58 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.25 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.06 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.31 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5290), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC15A3]] | +0.91 | +0.87 / +0.91 | both halves | 7e-06 | **novel candidate** |
| [[EPSTI1]] | +0.91 | +0.88 / +0.90 | both halves | 7e-06 | STRING 550 |
| [[OAS2]] | +0.88 | +0.85 / +0.89 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 755 |
| [[XAF1]] | +0.88 | +0.84 / +0.89 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 796 |
| [[TRANK1]] | +0.88 | +0.86 / +0.87 | both halves | 7e-06 | **novel candidate** |
| [[IFI35]] | +0.88 | +0.83 / +0.89 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 583 |
| [[PARP10]] | +0.87 | +0.80 / +0.90 | both halves | 7e-06 | **novel candidate** |
| [[USP18]] | +0.87 | +0.81 / +0.88 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 516 |
| [[IFIT3]] | +0.86 | +0.84 / +0.87 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 828 |
| [[TMEM140]] | +0.86 | +0.79 / +0.87 | both halves | 7e-06 | **novel candidate** |
| [[MX1]] | +0.86 | +0.82 / +0.88 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 713 |
| [[OAS1]] | +0.86 | +0.83 / +0.88 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 691 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*44 arrows, 44 of them with an alert ⚠; grade A 0, B 18, C 26. Shown: the 12 strongest; 32 more arrows (32 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LMO2]] | B | LMO2 activity strengthens TRIM22's drug response | lines that do not express LMO2 (11) vs lines expressing it (19) | the lines without LMO2 respond 0.62× as strongly (z diff +2.33); strongest at Tofacitinib 0.5 µM: 0.48x vs 0.19x (z diff +3.8) | 0.006 | ⚠ within organs, on part of the lines; also absent: TNFSF10, SAA1, SAA4; maybe low, not absent; target measured in part of the lines |
| [[LMO2]] | B | LMO2 activity raises TRIM22's level | lines that do not express LMO2 (24) vs lines expressing it (26) | 3.47× lower at baseline in the lines without LMO2 | 0.007 | ⚠ within organs, on part of the lines; also absent: TNFSF10, SAA1, SAA4; maybe low, not absent |
| [[IFIT3]] | B | IFIT3 activity raises TRIM22's level | lines that do not express IFIT3 (8) vs lines expressing it (42) | 4.89× lower at baseline in the lines without IFIT3 | 0.010 | ⚠ within organs, on part of the lines; also absent: GBP2, IFIT2, TRIM38; maybe low, not absent |
| [[IDO1]] | B | IDO1 activity raises TRIM22's level | lines that do not express IDO1 (28) vs lines expressing it (22) | 3.70× lower at baseline in the lines without IDO1 | 0.013 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, DKK3 |
| [[PLSCR1]] | B | PLSCR1 activity raises TRIM22's level | lines that do not express PLSCR1 (8) vs lines expressing it (42) | 4.83× lower at baseline in the lines without PLSCR1 | 0.021 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent |
| [[CMPK2]] | B | CMPK2 activity raises TRIM22's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 3.27× lower at baseline in the lines without CMPK2 | 0.029 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[IFI44]] | B | IFI44 activity raises TRIM22's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 3.26× lower at baseline in the lines without IFI44 | 0.030 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[CTSS]] | B | CTSS activity raises TRIM22's level | lines that do not express CTSS (15) vs lines expressing it (35) | 2.82× lower at baseline in the lines without CTSS | 0.035 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[RSAD2]] | B | RSAD2 activity raises TRIM22's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 3.00× lower at baseline in the lines without RSAD2 | 0.043 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[DDX60L]] | B | DDX60L activity raises TRIM22's level | lines that do not express DDX60L (7) vs lines expressing it (43) | 3.93× lower at baseline in the lines without DDX60L | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000287188, ENSG00000291144; maybe low, not absent |
| [[OASL]] | B | OASL activity raises TRIM22's level | lines that do not express OASL (10) vs lines expressing it (40) | 3.78× lower at baseline in the lines without OASL | 0.051 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |
| [[NRIR]] | B | NRIR activity raises TRIM22's level | lines that do not express NRIR (14) vs lines expressing it (36) | 2.67× lower at baseline in the lines without NRIR | 0.057 | ⚠ within organs, on part of the lines; also absent: CMPK2, TSPAN7 |

### Downstream of this gene

*120 arrows, 120 of them with an alert ⚠; grade A 0, B 94, C 26. Shown: the 12 strongest; 108 more arrows (108 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HERC6]] | B | TRIM22 activity raises HERC6's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 2.82× lower at baseline in the lines without TRIM22 | 2e-04 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[CMPK2]] | B | TRIM22 activity raises CMPK2's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 3.28× lower at baseline in the lines without TRIM22 | 6e-04 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[NLRC5]] | B | TRIM22 activity raises NLRC5's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 2.51× lower at baseline in the lines without TRIM22 | 6e-04 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[PLSCR1]] | B | TRIM22 activity raises PLSCR1's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 3.15× lower at baseline in the lines without TRIM22 | 0.001 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[DDX60L]] | B | TRIM22 activity raises DDX60L's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 3.09× lower at baseline in the lines without TRIM22 | 0.001 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[DDX60]] | B | TRIM22 activity raises DDX60's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 2.65× lower at baseline in the lines without TRIM22 | 0.001 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[PML]] | B | TRIM22 activity raises PML's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 2.12× lower at baseline in the lines without TRIM22 | 0.001 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[LAP3]] | B | TRIM22 activity raises LAP3's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 1.88× lower at baseline in the lines without TRIM22 | 0.001 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[SAMD9]] | B | TRIM22 activity raises SAMD9's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 3.73× lower at baseline in the lines without TRIM22 | 0.002 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[N4BP1]] | B | TRIM22 activity raises N4BP1's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 1.31× lower at baseline in the lines without TRIM22 | 0.002 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[PARP14]] | B | TRIM22 activity raises PARP14's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 2.47× lower at baseline in the lines without TRIM22 | 0.002 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[PARP9]] | B | TRIM22 activity raises PARP9's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 2.64× lower at baseline in the lines without TRIM22 | 0.003 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.906). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.7, 52.9); signed map (63.8, 30.8). **Vector** length 154, 58.1% of its response variance represented; |z| ≥ 3 in 1,531 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.76 to 56); *interferon gamma response* (hallmark, mean cos +0.76 to 60); *interferon* (control, mean cos +0.82 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +7.6 | +5.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +6.3 | +3.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.1 | -1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.1 | +5.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.8 | +10.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.8 | +7.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.8 | +6.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.7 | +6.5 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -10.4 | -16.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -8.9 | -13.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -8.6 | -13.4 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -8.5 | -13.4 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -8.2 | -12.4 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 22 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:5,689,610-5,737,089 (+) |
| Ensembl biotype | protein_coding |
| Also known as | STAF50, GPSTAF50, RNF94 |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; Minor histocompatibility antigens; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Interferon gamma signaling; Interferon Signaling; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IYM9](https://www.uniprot.org/uniprotkb/Q8IYM9) (E3 ubiquitin-protein ligase TRIM22):

> Interferon-induced E3 ubiquitin ligase that plays important roles in innate and adaptive immunity. Restricts the replication of many viruses including HIV-1, encephalomyocarditis virus (EMCV), hepatitis B virus (HBV), hepatitis C virus (HCV) or Zika virus (ZIKV). Mechanistically, negatively regulates HCV replication by promoting ubiquitination and subsequent degradation of viral NS5A. Also acts by promoting the degradation of Zika virus NS1 and NS3 proteins through proteasomal degradation. Acts …

**Summary**, from NCBI Gene [10346](https://www.ncbi.nlm.nih.gov/gene/10346):

> The protein encoded by this gene is a member of the tripartite motif (TRIM) family. The TRIM motif includes three zinc-binding domains, a RING, a B-box type 1 and a B-box type 2, and a coiled-coil region. This protein localizes to the cytoplasm and its expression is induced by interferon. The protein is involved in innate immunity against different DNA and RNA viruses. [provided by RefSeq, Oct 2021]

**Accessions** — [HGNC:16379](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16379) · Entrez [10346](https://www.ncbi.nlm.nih.gov/gene/10346) · UniProt [Q8IYM9](https://www.uniprot.org/uniprotkb/Q8IYM9) · Ensembl [ENSG00000132274](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132274)

## Data

Gene col 5290: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5290); `tables/drug_effects.parquet` (81 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5290, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5290]; `tensor/DDL_lfc|DDL_z.npy` [5290]; `embed/gene_vectors.npy` [5290]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5290 or target_col == 5290). Every well: [[TRIM22 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM22.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
