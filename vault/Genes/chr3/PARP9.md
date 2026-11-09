---
symbol: "PARP9"
type: "gene"
col: 6185
ensembl_id: "ENSG00000138496"
name: "poly(ADP-ribose) polymerase family member 9"
location: "3q21.1"
module: 32
arm: "+"
pooled_cpm: 89.72
n_lines_expressing: 43
n_dd_up: 26
n_dd_down: 61
n_dd_up_clean: 26
n_dd_down_clean: 47
in_vector_space: true
direction_upstream: 47
direction_downstream: 74
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# PARP9

*poly(ADP-ribose) polymerase family member 9* — 3q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 2.07× (z +8.6, q 7e-15, up in 39 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 61 drug-doses (14 with an alert ⚠); the strongest is [[Tofacitinib (drug)]] 5 µM: 0.247× (z -24.0, q 0e+00, down in 37 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MX1]] (+0.95, fdr 7e-06), [[CMPK2]] (+0.94, fdr 7e-06), [[OAS3]] (+0.94, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 47 arrows point to it, the strongest [[OAS2]] → it (grade B ⚠); 74 go from it, the strongest it → [[UNC93B1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, none with an alert; shown: the 15 strongest. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6185.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **2.07×** | +8.6 | 7e-15 | 39/40 (Hs 766T, NCI-H23, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.65×** | +6.1 | 3e-07 | 36/40 (Hs 766T, AsPC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.61×** | +5.8 | 1e-06 | 27/41 (NCI-H2347, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.54×** | +5.5 | 4e-06 | 37/42 (Hs 766T, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.48×** | +5.4 | 9e-06 | 35/43 (Hs 766T, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.35×** | +5.2 | 2e-05 | 30/41 (HS-578T, Hs 766T, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.39×** | +5.1 | 2e-05 | 34/41 (Hs 766T, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.41×** | +5.1 | 3e-05 | 33/41 (Hs 766T, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.54×** | +5.1 | 3e-05 | 31/40 (Hs 766T, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.49×** | +4.9 | 7e-05 | 29/40 (NCI-H2347, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.33×** | +4.8 | 7e-05 | 31/42 (Hs 766T, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.45×** | +4.5 | 3e-04 | 26/42 (Hs 766T, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.43×** | +4.1 | 0.002 | 26/41 (Hs 766T, AsPC-1, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 0.05 µM |  | **1.43×** | +4.1 | 0.002 | 31/42 (Hs 766T, HCT15, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.42×** | +4.0 | 0.003 | 29/41 (Hs 766T, CFPAC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 62 in all, 14 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 61 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6185.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | **0.247×** | -24.0 | 0e+00 | 37/42 (LoVo, COLO 205, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.168×** | -21.6 | 0e+00 | 40/41 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.217×** | -18.6 | 0e+00 | 41/41 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.341×** | -18.4 | 0e+00 | 36/42 (COLO 205, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.254×** | -16.6 | 0e+00 | 39/41 (LoVo, A549, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.282×** | -15.3 | 0e+00 | 38/41 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.431×** | -14.4 | 3e-45 | 34/41 (A549, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~24% here); composition shift |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.315×** | -14.0 | 1e-42 | 37/41 (BT-474, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.329×** | -13.5 | 1e-39 | 37/42 (NCI-H23, A549, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.344×** | -12.9 | 2e-36 | 38/42 (NCI-H23, BT-474, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.503×** | -11.8 | 3e-30 | 32/41 (NCI-H1573, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib (drug)]] 5 µM |  | **0.226×** | -9.4 | 2e-19 | 32/40 (BT-474, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.445×** | -9.4 | 2e-19 | 30/40 (A549, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.479×** | -8.9 | 2e-17 | 35/40 (RKO, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.476×** | -8.5 | 8e-16 | 36/41 (MIA PaCa-2, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.516×** | -8.0 | 4e-14 | 32/41 (NCI-H23, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6185. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 213 | 0 | 25 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0612× (z -29.0) |
| [[NCI-H23 (line)]] | alt | 105 | 0 | 24 (7 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.137× (z -20.9) |
| [[A549 (line)]] | wt | 141 | 0 | 23 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0536× (z -34.2) |
| [[SNU-423 (line)]] | alt | 128 | 0 | 21 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -20.0) |
| [[RKO (line)]] | wt | 89.4 | 0 | 20 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0514× (z -20.8) |
| [[MIA PaCa-2 (line)]] | alt | 159 | 0 | 19 (5 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.129× (z -20.8) |
| [[BT-474 (line)]] | alt | 133 | 0 | 18 (3 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.161× (z -18.9) |
| [[HS-578T (line)]] | alt | 115 | 3 (1 ⚠) | 15 (4 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.52× (z +11.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 3.08× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.113× (z -17.2) |
| [[NCI-H1573 (line)]] | alt | 121 | 0 | 18 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0993× (z -28.2) |
| [[RPMI-7951 (line)]] | alt | 169 | 0 | 18 (3 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.179× (z -22.5) |
| [[A-172 (line)]] | wt | 163 | 0 | 17 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.102× (z -20.0) |
| [[NCI-H1792 (line)]] | alt | 90.1 | 0 | 17 (6 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.194× (z -18.2) |
| [[SNU-1 (line)]] | wt | 82.1 | 0 | 15 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -17.3) |
| [[COLO 205 (line)]] | alt | 335 | 0 | 14 (1 ⚠) | — | [[Tofacitinib (citrate) (drug)]] 5 µM 0.172× (z -23.4) |
| [[A498 (line)]] | wt | 78.6 | 0 | 13 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -18.6) |
| [[C-33 A (line)]] | alt | 87.8 | 0 | 13 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0501× (z -19.0) |
| [[CFPAC-1 (line)]] | alt | 202 | 0 | 12 (3 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.176× (z -21.8) |
| [[Hs 766T (line)]] | wt | 98.6 | 1 | 10 | [[Cobimetinib (drug)]] 5 µM 3.32× (z +8.6) | [[Tofacitinib (drug)]] 5 µM 0.204× (z -16.8) |
| [[NCI-H2347 (line)]] | alt | 132 | 3 (2 ⚠) | 8 | [[Harringtonine (drug)]] 5 µM 3.48× (z +10.1) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.31× (z +10.1) | [[Tofacitinib (drug)]] 5 µM 0.215× (z -18.4) |
| [[PANC-1 (line)]] | alt | 50.3 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -26.6) |
| [[SK-MEL-2 (line)]] | alt | 153 | 0 | 11 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.104× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.246× (z -16.3) |
| [[AsPC-1 (line)]] | alt | 82.9 | 0 | 10 (2 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.235× (z -15.8) |
| [[KATO III (line)]] | alt | 155 | 0 | 9 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0900× (z -19.6) |
| [[SW1417 (line)]] | alt | 128 | 0 | 9 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -15.6) |
| [[HepG2_C3A (line)]] | wt | 65.5 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -13.0) |
| [[Panc 03.27 (line)]] | alt | 203 | 0 | 7 | — | [[Tofacitinib (drug)]] 5 µM 0.266× (z -15.0) |
| [[LOX-IMVI (line)]] | wt | 42.2 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -15.6) |
| [[SHP-77 (line)]] | alt | 66.8 | 0 | 6 | — | [[Tofacitinib (drug)]] 5 µM 0.168× (z -14.8) |
| [[CHP-212 (line)]] | wt | 77.8 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.0709× (z -11.8) |
| [[HT-29 (line)]] | alt | 47.6 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -12.8) |
| [[J82 (line)]] | alt | 58.6 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 5.86× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | [[Tofacitinib (drug)]] 5 µM 0.296× (z -11.6) |
| [[A-427 (line)]] | wt | 36.2 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.268× (z -10.6) |
| [[C32 (line)]] | wt | 84.8 | 0 | 4 | — | [[Auranofin (drug)]] 5 µM 0.150× (z -13.0) |
| [[SW 900 (line)]] | alt | 47.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -12.3) |
| [[HCT15 (line)]] | alt | 45.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.165× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 32.4 | 1 (1 ⚠) | 1 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.77× (z +8.7) ⚠ toxic; cell-cycle shift, explains ~5% of this change | [[Panobinostat (drug)]] 5 µM 0.265× (z -11.8) |
| [[AN3 CA (line)]] | alt | 19.8 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.3 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.2 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 22.4 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 21.0 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6185), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MX1]] | +0.95 | +0.90 / +0.96 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 847 |
| [[CMPK2]] | +0.94 | +0.89 / +0.96 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 769 |
| [[OAS3]] | +0.94 | +0.92 / +0.95 | both halves | 7e-06 | STRING 861 |
| [[OAS2]] | +0.94 | +0.86 / +0.96 | both halves | 7e-06 | STRING 875 |
| [[EIF2AK2]] | +0.94 | +0.89 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 774 |
| [[IFIT1]] | +0.94 | +0.90 / +0.94 | both halves | 7e-06 | STRING 751 |
| [[OAS1]] | +0.94 | +0.89 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 870 |
| [[IFI35]] | +0.93 | +0.89 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 882 |
| [[USP18]] | +0.93 | +0.88 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 698 |
| [[IFI44]] | +0.92 | +0.87 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 929 |
| [[PARP14]] | +0.92 | +0.89 / +0.94 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 942 |
| [[HERC6]] | +0.92 | +0.89 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 663 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*47 arrows, 47 of them with an alert ⚠; grade A 0, B 37, C 10. Shown: the 12 strongest; 35 more arrows (35 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OAS2]] | B | OAS2 activity raises PARP9's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 3.16× lower at baseline in the lines without OAS2 | 2e-04 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[OAS1]] | B | OAS1 activity raises PARP9's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 3.29× lower at baseline in the lines without OAS1 | 3e-04 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[IFI6]] | B | IFI6 activity raises PARP9's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 3.63× lower at baseline in the lines without IFI6 | 6e-04 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[BATF2]] | B | BATF2 activity raises PARP9's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 2.61× lower at baseline in the lines without BATF2 | 0.001 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |
| [[RASGRP3]] | B | RASGRP3 activity raises PARP9's level | lines that do not express RASGRP3 (16) vs lines expressing it (34) | 2.72× lower at baseline in the lines without RASGRP3 | 0.002 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent |
| [[TRIM22]] | B | TRIM22 activity raises PARP9's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 2.64× lower at baseline in the lines without TRIM22 | 0.003 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[CD5L]] | B | CD5L activity raises PARP9's level | lines that do not express CD5L (23) vs lines expressing it (27) | 2.32× lower at baseline in the lines without CD5L | 0.004 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent |
| [[FBXO39]] | B | FBXO39 activity raises PARP9's level | lines that do not express FBXO39 (16) vs lines expressing it (34) | 2.37× lower at baseline in the lines without FBXO39 | 0.004 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3 |
| [[GBP4]] | B | GBP4 activity raises PARP9's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 2.23× lower at baseline in the lines without GBP4 | 0.006 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[SAMD9]] | B | SAMD9 activity raises PARP9's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 2.40× lower at baseline in the lines without SAMD9 | 0.006 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[MX1]] | B | MX1 activity raises PARP9's level | lines that do not express MX1 (19) vs lines expressing it (31) | 2.57× lower at baseline in the lines without MX1 | 0.006 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[CCDC194]] | B | CCDC194 activity raises PARP9's level | lines that do not express CCDC194 (19) vs lines expressing it (31) | 2.22× lower at baseline in the lines without CCDC194 | 0.007 | ⚠ within organs, on part of the lines; also absent: BST2, DEPP1, TRIM22 |

### Downstream of this gene

*74 arrows, 74 of them with an alert ⚠; grade A 0, B 58, C 16. Shown: the 12 strongest; 62 more arrows (62 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UNC93B1]] | B | PARP9 activity raises UNC93B1's level | lines that do not express PARP9 (7) vs lines expressing it (43) | 2.04× lower at baseline in the lines without PARP9 | 0.001 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent |
| [[DTX3L]] | B | PARP9 activity raises DTX3L's level | lines that do not express PARP9 (7) vs lines expressing it (43) | 3.15× lower at baseline in the lines without PARP9 | 0.001 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent |
| [[PARP10]] | B | PARP9 activity raises PARP10's level | lines that do not express PARP9 (7) vs lines expressing it (43) | 2.37× lower at baseline in the lines without PARP9 | 0.001 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent |
| [[PARP14]] | B | PARP9 activity raises PARP14's level | lines that do not express PARP9 (7) vs lines expressing it (43) | 3.18× lower at baseline in the lines without PARP9 | 0.002 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent |
| [[TRIM25]] | B | PARP9 activity raises TRIM25's level | lines that do not express PARP9 (7) vs lines expressing it (43) | 2.25× lower at baseline in the lines without PARP9 | 0.002 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent |
| [[EIF2AK2]] | B | PARP9 activity raises EIF2AK2's level | lines that do not express PARP9 (7) vs lines expressing it (43) | 2.35× lower at baseline in the lines without PARP9 | 0.004 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent |
| [[SP110]] | B | PARP9 activity raises SP110's level | lines that do not express PARP9 (7) vs lines expressing it (43) | 3.42× lower at baseline in the lines without PARP9 | 0.004 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent |
| [[HELZ2]] | B | PARP9 activity raises HELZ2's level | lines that do not express PARP9 (7) vs lines expressing it (43) | 2.85× lower at baseline in the lines without PARP9 | 0.004 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent |
| [[TRIM14]] | B | PARP9 activity raises TRIM14's level | lines that do not express PARP9 (7) vs lines expressing it (43) | 2.49× lower at baseline in the lines without PARP9 | 0.005 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent |
| [[REC8]] | B | PARP9 activity raises REC8's level | lines that do not express PARP9 (7) vs lines expressing it (43) | 2.24× lower at baseline in the lines without PARP9 | 0.008 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent |
| [[ADAR]] | B | PARP9 activity strengthens ADAR's drug response | lines that do not express PARP9 (7) vs lines expressing it (42) | the lines without PARP9 respond 0.33× as strongly (z diff +3.46); strongest at Auranofin 5 µM: 1.06x vs 0.66x (z diff +6.7) | 0.010 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[IRF9]] | B | PARP9 activity raises IRF9's level | lines that do not express PARP9 (7) vs lines expressing it (43) | 2.41× lower at baseline in the lines without PARP9 | 0.010 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.967). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.5, 53.8); signed map (64.7, 31.8). **Vector** length 154, 64.6% of its response variance represented; |z| ≥ 3 in 1,975 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon gamma response* (hallmark, mean cos +0.82 to 60); *interferon* (control, mean cos +0.89 to 23); *Interferon Signaling* (reactome, mean cos +0.83 to 45).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +11.3 | +5.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +7.9 | +8.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +7.9 | -0.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +7.2 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.9 | +1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.9 | +5.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.8 | +5.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +4.6 | +6.1 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -12.4 | -24.0 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -10.9 | -18.4 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -10.5 | -14.0 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -10.5 | -12.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -9.9 | -11.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -8.2 | -13.5 |

## What is on record

|  |  |
|---|---|
| Name | poly(ADP-ribose) polymerase family member 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.1 — chr3:122,527,924-122,564,577 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BAL, BAL1, ARTD9 |
| Gene groups (HGNC) | Poly(ADP-ribose) polymerases; Macro domain containing |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE |
| Reactome | 12 pathways, smallest: Maturation of nucleoprotein_9683610; Maturation of nucleoprotein_9694631; Nicotinate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IXQ6](https://www.uniprot.org/uniprotkb/Q8IXQ6) (Protein mono-ADP-ribosyltransferase PARP9):

> ADP-ribosyltransferase which, in association with E3 ligase DTX3L, plays a role in DNA damage repair and in immune responses including interferon-mediated antiviral defenses. Within the complex, enhances DTX3L E3 ligase activity which is further enhanced by PARP9 binding to poly(ADP-ribose). In association with DTX3L and in presence of E1 and E2 enzymes, mediates NAD(+)-dependent mono-ADP-ribosylation of ubiquitin which prevents ubiquitin conjugation to substrates such as histones. During DNA …

**Summary**, from NCBI Gene [83666](https://www.ncbi.nlm.nih.gov/gene/83666):

> Enables several functions, including STAT family protein binding activity; pentosyltransferase activity; and transcription corepressor activity. Involved in several processes, including positive regulation of tyrosine phosphorylation of STAT protein; regulation of defense response; and regulation of gene expression. Located in cytosol; nucleoplasm; and site of DNA damage. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24118](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24118) · Entrez [83666](https://www.ncbi.nlm.nih.gov/gene/83666) · UniProt [Q8IXQ6](https://www.uniprot.org/uniprotkb/Q8IXQ6) · Ensembl [ENSG00000138496](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138496)

## Data

Gene col 6185: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6185); `tables/drug_effects.parquet` (90 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6185, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6185]; `tensor/DDL_lfc|DDL_z.npy` [6185]; `embed/gene_vectors.npy` [6185]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6185 or target_col == 6185). Every well: [[PARP9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PARP9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
