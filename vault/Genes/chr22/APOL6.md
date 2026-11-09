---
symbol: "APOL6"
type: "gene"
col: 13323
ensembl_id: "ENSG00000221963"
name: "apolipoprotein L6"
location: "22q12.3"
module: 70
arm: "+"
pooled_cpm: 67.98
n_lines_expressing: 44
n_dd_up: 32
n_dd_down: 43
n_dd_up_clean: 28
n_dd_down_clean: 36
in_vector_space: true
direction_upstream: 51
direction_downstream: 45
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# APOL6

*apolipoprotein L6* — 22q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.90× (z +11.4, q 3e-27, up in 32 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 43 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.181× (z -30.3, q 0e+00, down in 42 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NMI]] (+0.82, fdr 7e-06), [[GBP1]] (+0.81, fdr 7e-06), [[PSMB8]] (+0.81, fdr 7e-06).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 51 arrows point to it, the strongest [[PLAAT4]] → it (grade B ⚠); 45 go from it, the strongest it → [[SAMD9L]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13323.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.90×** | +11.4 | 3e-27 | 32/42 (PANC-1, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.59×** | +7.9 | 1e-12 | 29/41 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.42×** | +7.4 | 2e-11 | 32/42 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.46×** | +7.3 | 4e-11 | 33/43 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.51×** | +7.3 | 4e-11 | 25/42 (NCI-H2347, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.49×** | +7.2 | 7e-11 | 30/42 (CFPAC-1, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.51×** | +7.0 | 1e-10 | 29/42 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.33×** | +7.0 | 2e-10 | 31/42 (AsPC-1, CFPAC-1, …) | all doses, flat |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.48×** | +7.0 | 2e-10 | 31/42 (HEC-1-A, KATO III, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.36×** | +6.7 | 1e-09 | 27/42 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.46×** | +6.4 | 1e-08 | 25/42 (AsPC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.43×** | +6.3 | 2e-08 | 29/43 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.34×** | +5.2 | 1e-05 | 22/41 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.34×** | +5.1 | 1e-05 | 18/41 (SW 900, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 0.05 µM |  | **1.35×** | +5.0 | 2e-05 | 20/42 (AsPC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.22×** | +4.9 | 4e-05 | 19/42 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 62 in all, 10 with an alert ⚠; shown: the 15 strongest. 43 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13323.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.181×** | -30.3 | 0e+00 | 42/42 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.196×** | -28.9 | 0e+00 | 42/42 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.224×** | -26.5 | 0e+00 | 42/42 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.396×** | -23.2 | 0e+00 | 36/41 (KATO III, A498, …) | top dose only | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.405×** | -16.0 | 0e+00 | 41/42 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.455×** | -14.0 | 2e-42 | 40/42 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.520×** | -11.6 | 3e-29 | 36/42 (SNU-423, MIA PaCa-2, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.639×** | -11.2 | 2e-27 | 30/42 (A498, COLO 205, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.646×** | -11.0 | 4e-26 | 30/42 (CFPAC-1, COLO 205, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.700×** | -9.0 | 2e-17 | 31/42 (A498, MIA PaCa-2, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.705×** | -8.8 | 9e-17 | 32/43 (CFPAC-1, A549, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.604×** | -8.6 | 4e-16 | 25/41 (A498, SW1417, …) | top dose only | cell-cycle shift (explains ~21% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.432×** | -7.5 | 2e-12 | 26/43 (A498, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.660×** | -7.4 | 6e-12 | 23/42 (AsPC-1, KATO III, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.446×** | -7.3 | 1e-11 | 31/42 (KATO III, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13323. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 186 | 0 | 17 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -35.0) |
| [[A498 (line)]] | wt | 165 | 0 | 15 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.108× (z -30.7) |
| [[MIA PaCa-2 (line)]] | alt | 66.3 | 1 (1 ⚠) | 14 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.53× (z +10.1) ⚠ position not correctable | [[Panobinostat (drug)]] 5 µM 0.0922× (z -16.4) |
| [[LoVo (line)]] | wt | 166 | 0 | 13 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0684× (z -29.6) |
| [[SNU-423 (line)]] | alt | 113 | 1 (1 ⚠) | 12 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.88× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.142× (z -17.0) |
| [[COLO 205 (line)]] | alt | 234 | 0 | 11 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0848× (z -21.5) |
| [[H4 (line)]] | wt | 70.4 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -15.5) |
| [[A549 (line)]] | wt | 50.4 | 0 | 10 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -18.2) |
| [[AsPC-1 (line)]] | alt | 58.2 | 4 | 6 | [[Trametinib (drug)]] 0.5 µM 2.85× (z +9.6) | [[Belinostat (drug)]] 5 µM 0.177× (z -13.2) |
| [[NCI-H2347 (line)]] | alt | 121 | 4 (2 ⚠) | 6 | [[Harringtonine (drug)]] 0.5 µM 3.06× (z +12.7) | [[Panobinostat (drug)]] 0.5 µM 0.263× (z -15.3) |
| [[PANC-1 (line)]] | alt | 56.8 | 1 | 9 | [[Harringtonine (drug)]] 0.5 µM 3.59× (z +15.3) | [[Panobinostat (drug)]] 5 µM 0.213× (z -18.6) |
| [[A-172 (line)]] | wt | 63.6 | 2 | 6 | [[Homoharringtonine (drug)]] 0.05 µM 2.53× (z +9.4) | [[Panobinostat (drug)]] 0.5 µM 0.0811× (z -25.6) |
| [[CFPAC-1 (line)]] | alt | 131 | 1 | 7 | [[Binimetinib (drug)]] 5 µM 2.26× (z +8.6) | [[Tofacitinib (drug)]] 5 µM 0.348× (z -15.0) |
| [[HT-29 (line)]] | alt | 88.5 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -26.0) |
| [[SW1417 (line)]] | alt | 86.9 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -28.8) |
| [[HEC-1-A (line)]] | alt | 50.0 | 3 (1 ⚠) | 4 | [[Harringtonine (drug)]] 0.5 µM 2.89× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.227× (z -14.0) |
| [[HS-578T (line)]] | alt | 116 | 3 (1 ⚠) | 4 | [[Harringtonine (drug)]] 0.5 µM 5.24× (z +14.5) | [[Panobinostat (drug)]] 5 µM 0.183× (z -14.9) |
| [[NCI-H1792 (line)]] | alt | 59.7 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0879× (z -27.7) |
| [[SHP-77 (line)]] | alt | 36.9 | 0 | 6 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0808× (z -12.7) |
| [[SW480 (line)]] | alt | 18.8 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -16.8) |
| [[RPMI-7951 (line)]] | alt | 82.7 | 1 | 4 | [[Harringtonine (drug)]] 0.5 µM 3.24× (z +9.4) | [[Panobinostat (drug)]] 0.5 µM 0.138× (z -15.8) |
| [[C32 (line)]] | wt | 44.0 | 1 | 3 | [[Harringtonine (drug)]] 0.5 µM 3.55× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.233× (z -10.9) |
| [[LS 180 (line)]] | wt | 94.7 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0829× (z -19.7) |
| [[RKO (line)]] | wt | 21.6 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.0472× (z -15.0) |
| [[SW 900 (line)]] | alt | 37.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -12.6) |
| [[HCT15 (line)]] | alt | 50.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0922× (z -14.9) |
| [[Hs 766T (line)]] | wt | 135 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.217× (z -14.2) |
| [[NCI-H1573 (line)]] | alt | 35.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.146× (z -13.3) |
| [[NCI-H460 (line)]] | wt | 27.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.187× (z -15.0) |
| [[Panc 03.27 (line)]] | alt | 84.8 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.353× (z -9.8) |
| [[SW 1088 (line)]] | alt | 159 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.102× (z -9.5) |
| [[AN3 CA (line)]] | alt | 21.7 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0632× (z -8.7) |
| [[BT-474 (line)]] | alt | 21.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -9.0) |
| [[CHP-212 (line)]] | wt | 30.9 | 0 | 2 | — | [[Orlistat (drug)]] 0.05 µM 0.0671× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 24.4 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.159× (z -13.6) |
| [[SW48 (line)]] | wt | 29.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0541× (z -14.7) |
| [[HepG2_C3A (line)]] | wt | 35.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -9.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 53.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.355× (z -8.6) |
| [[SNU-1 (line)]] | wt | 23.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.121× (z -9.4) |
| [[A-427 (line)]] | wt | 8.93 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 13.6 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.4 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.79 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13323), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NMI]] | +0.82 | +0.71 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[GBP1]] | +0.81 | +0.76 / +0.80 | both halves | 7e-06 | STRING 559 |
| [[PSMB8]] | +0.81 | +0.72 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[PARP14]] | +0.81 | +0.69 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[GBP4]] | +0.81 | +0.72 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 551 |
| [[SLC15A3]] | +0.81 | +0.68 / +0.85 | both halves | 7e-06 |  |
| [[EPSTI1]] | +0.80 | +0.66 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[IFI35]] | +0.80 | +0.68 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[SAMD9L]] | +0.79 | +0.66 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[XAF1]] | +0.79 | +0.64 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 494 |
| [[PSMB10]] | +0.79 | +0.72 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[TRANK1]] | +0.79 | +0.72 / +0.79 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*51 arrows, 51 of them with an alert ⚠; grade A 0, B 46, C 5. Shown: the 12 strongest; 39 more arrows (39 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLAAT4]] | B | PLAAT4 activity raises APOL6's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 3.00× lower at baseline in the lines without PLAAT4 | 3e-04 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[GBP4]] | B | GBP4 activity raises APOL6's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 2.55× lower at baseline in the lines without GBP4 | 0.001 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[RSAD2]] | B | RSAD2 activity raises APOL6's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 2.97× lower at baseline in the lines without RSAD2 | 0.001 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[IFI44]] | B | IFI44 activity raises APOL6's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 2.53× lower at baseline in the lines without IFI44 | 0.001 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[GBP1]] | B | GBP1 activity raises APOL6's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 2.59× lower at baseline in the lines without GBP1 | 0.002 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[OAS1]] | B | OAS1 activity raises APOL6's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.20× lower at baseline in the lines without OAS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[APOL1]] | B | APOL1 activity raises APOL6's level | lines that do not express APOL1 (24) vs lines expressing it (26) | 2.85× lower at baseline in the lines without APOL1 | 0.004 | ⚠ within organs, on part of the lines; also absent: POU5F1, UGT1A6, NMRAL2P-1 |
| [[CASP10]] | B | CASP10 activity raises APOL6's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 2.60× lower at baseline in the lines without CASP10 | 0.004 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[SAMD9L]] | B | SAMD9L activity raises APOL6's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 2.54× lower at baseline in the lines without SAMD9L | 0.004 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[XAF1]] | B | XAF1 activity raises APOL6's level | lines that do not express XAF1 (14) vs lines expressing it (36) | 2.65× lower at baseline in the lines without XAF1 | 0.006 | ⚠ within organs, on part of the lines; also absent: SLC15A3, TRIM22, FBXO39 |
| [[OAS3]] | B | OAS3 activity raises APOL6's level | lines that do not express OAS3 (5) vs lines expressing it (45) | 3.41× lower at baseline in the lines without OAS3 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000280007, PARP9, USP18 |
| [[EPSTI1]] | B | EPSTI1 activity raises APOL6's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 2.60× lower at baseline in the lines without EPSTI1 | 0.007 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |

### Downstream of this gene

*45 arrows, 45 of them with an alert ⚠; grade A 0, B 40, C 5. Shown: the 12 strongest; 33 more arrows (33 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAMD9L]] | B | APOL6 activity raises SAMD9L's level | lines that do not express APOL6 (6) vs lines expressing it (44) | 5.51× lower at baseline in the lines without APOL6 | 0.006 | ⚠ within organs, on part of the lines; also absent: KLF4, S100A13, LGALS3BP; maybe low, not absent |
| [[RSAD2]] | B | APOL6 activity raises RSAD2's level | lines that do not express APOL6 (6) vs lines expressing it (44) | 4.50× lower at baseline in the lines without APOL6 | 0.007 | ⚠ within organs, on part of the lines; also absent: KLF4, S100A13, LGALS3BP; maybe low, not absent |
| [[OAS1]] | B | APOL6 activity raises OAS1's level | lines that do not express APOL6 (6) vs lines expressing it (44) | 3.46× lower at baseline in the lines without APOL6 | 0.009 | ⚠ within organs, on part of the lines; also absent: KLF4, S100A13, LGALS3BP; maybe low, not absent |
| [[SAMD9]] | B | APOL6 activity raises SAMD9's level | lines that do not express APOL6 (6) vs lines expressing it (44) | 4.18× lower at baseline in the lines without APOL6 | 0.009 | ⚠ within organs, on part of the lines; also absent: KLF4, S100A13, LGALS3BP; maybe low, not absent |
| [[TRANK1]] | B | APOL6 activity raises TRANK1's level | lines that do not express APOL6 (6) vs lines expressing it (44) | 3.14× lower at baseline in the lines without APOL6 | 0.012 | ⚠ within organs, on part of the lines; also absent: KLF4, S100A13, LGALS3BP; maybe low, not absent |
| [[IFI44]] | B | APOL6 activity raises IFI44's level | lines that do not express APOL6 (6) vs lines expressing it (44) | 3.03× lower at baseline in the lines without APOL6 | 0.014 | ⚠ within organs, on part of the lines; also absent: KLF4, S100A13, LGALS3BP; maybe low, not absent |
| [[TMEM140]] | B | APOL6 activity raises TMEM140's level | lines that do not express APOL6 (6) vs lines expressing it (44) | 2.79× lower at baseline in the lines without APOL6 | 0.014 | ⚠ within organs, on part of the lines; also absent: KLF4, S100A13, LGALS3BP; maybe low, not absent |
| [[APOL1]] | B | APOL6 activity raises APOL1's level | lines that do not express APOL6 (6) vs lines expressing it (44) | 4.29× lower at baseline in the lines without APOL6 | 0.018 | ⚠ within organs, on part of the lines; also absent: KLF4, S100A13, LGALS3BP; maybe low, not absent |
| [[SP140L]] | B | APOL6 activity raises SP140L's level | lines that do not express APOL6 (6) vs lines expressing it (44) | 3.01× lower at baseline in the lines without APOL6 | 0.019 | ⚠ within organs, on part of the lines; also absent: KLF4, S100A13, LGALS3BP; maybe low, not absent |
| [[DDX60]] | B | APOL6 activity raises DDX60's level | lines that do not express APOL6 (6) vs lines expressing it (44) | 2.49× lower at baseline in the lines without APOL6 | 0.023 | ⚠ within organs, on part of the lines; also absent: KLF4, S100A13, LGALS3BP; maybe low, not absent |
| [[GBP4]] | B | APOL6 activity raises GBP4's level | lines that do not express APOL6 (6) vs lines expressing it (44) | 4.09× lower at baseline in the lines without APOL6 | 0.028 | ⚠ within organs, on part of the lines; also absent: KLF4, S100A13, LGALS3BP; maybe low, not absent |
| [[APOL2]] | B | APOL6 activity raises APOL2's level | lines that do not express APOL6 (6) vs lines expressing it (44) | 2.27× lower at baseline in the lines without APOL6 | 0.030 | ⚠ within organs, on part of the lines; also absent: KLF4, S100A13, LGALS3BP; maybe low, not absent |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.809). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.2, 52.2); signed map (62.2, 30.2). **Vector** length 151, 54.5% of its response variance represented; |z| ≥ 3 in 1,705 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.56 to 19); *Antigen processing-Cross presentation* (reactome, mean cos +0.60 to 14); *Interferon gamma signaling* (reactome, mean cos +0.56 to 13).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +8.9 | +11.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +7.2 | +7.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.7 | +3.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.5 | +2.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | +6.5 | +3.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +6.3 | +7.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +6.2 | +7.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.8 | +6.7 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -8.5 | -11.0 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -7.0 | -7.3 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -6.7 | -8.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.7 | -14.0 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -6.5 | -7.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -6.1 | -11.6 |

## What is on record

|  |  |
|---|---|
| Name | apolipoprotein L6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.3 — chr22:35,648,446-35,668,404 (+) |
| Ensembl biotype | protein_coding |
| Also known as | APOL-VI, APOLVI |
| Gene groups (HGNC) | Apolipoproteins |
| Hallmark sets | INTERFERON_GAMMA_RESPONSE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BWW8](https://www.uniprot.org/uniprotkb/Q9BWW8) (Apolipoprotein L6):

> May affect the movement of lipids in the cytoplasm or allow the binding of lipids to organelles.

**Summary**, from NCBI Gene [80830](https://www.ncbi.nlm.nih.gov/gene/80830):

> This gene is a member of the apolipoprotein L gene family. The encoded protein is found in the cytoplasm, where it may affect the movement of lipids or allow the binding of lipids to organelles. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:14870](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14870) · Entrez [80830](https://www.ncbi.nlm.nih.gov/gene/80830) · UniProt [Q9BWW8](https://www.uniprot.org/uniprotkb/Q9BWW8) · Ensembl [ENSG00000221963](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000221963)

## Data

Gene col 13323: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13323); `tables/drug_effects.parquet` (105 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13323, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13323]; `tensor/DDL_lfc|DDL_z.npy` [13323]; `embed/gene_vectors.npy` [13323]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13323 or target_col == 13323). Every well: [[APOL6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APOL6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
