---
symbol: "DAB2"
type: "gene"
col: 7687
ensembl_id: "ENSG00000153071"
name: "DAB adaptor protein 2"
location: "5p13.1"
module: 13
arm: "+"
pooled_cpm: 52.05
n_lines_expressing: 32
n_dd_up: 11
n_dd_down: 35
n_dd_up_clean: 7
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 17
direction_downstream: 20
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# DAB2

*DAB adaptor protein 2* — 5p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.36× (z +7.0, q 1e-09, up in 16 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (19 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.408× (z -14.6, q 0e+00, down in 24 of 30 measured lines) ⚠ cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.530× (z -14.6, q 0e+00, down in 23 of 29 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTGFR]] (+0.62, fdr 1e-05), [[ATP8B2]] (+0.58, fdr 1e-05), [[C9]] (+0.55, fdr 1e-05, ⚠ read-through risk), [[GLIS1]] (+0.53, fdr 3e-05); moves opposite to [[SLC12A2-DT]] (-0.47, fdr 3e-05), [[ANK3]] (-0.44, fdr 5e-05), [[DCPS]] (-0.43, fdr 1e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[FBN1]] → it (grade B ⚠); 20 go from it, the strongest it → [[TNS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7687.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +7.0 | 1e-09 | 16/30 (SW480, NCI-H23, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.51×** | +6.7 | 7e-09 | 16/30 (SW480, Panc 03.27, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.64×** | +4.2 | 0.005 | 16/30 (AsPC-1, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.30×** | +4.1 | 0.007 | 13/29 (hTERT-HPNE, C32, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.55×** | +3.8 | 0.019 | 11/28 (J82, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.53×** | +3.6 | 0.025 | 14/29 (A-172, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.23×** | +3.5 | 0.040 | 15/30 (J82, hTERT-HPNE, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +3.2 | 0.084 | 9/30 (hTERT-HPNE, NCI-H1792, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 5 µM |  | **1.45×** | +3.2 | 0.085 | 9/30 (A-172, AsPC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.085 | 9/29 (COLO 205, HT-29, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.087 | 12/29 (AsPC-1, A-172, …) | two highest doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 19 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7687.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.408×** | -14.6 | 0e+00 | 24/30 (HS-578T, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.530×** | -14.6 | 0e+00 | 23/29 (HS-578T, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.456×** | -12.3 | 1e-32 | 23/29 (A498, HS-578T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.501×** | -11.2 | 3e-27 | 23/30 (A498, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.539×** | -10.1 | 9e-22 | 22/29 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.539×** | -9.7 | 3e-20 | 21/30 (A498, HS-578T, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.561×** | -9.4 | 4e-19 | 22/30 (NCI-H1792, SW 900, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.569×** | -9.2 | 3e-18 | 21/29 (H4, SW 900, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.672×** | -9.2 | 3e-18 | 18/29 (A498, SNU-423, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change | **0.592×** | -8.5 | 7e-16 | 21/28 (COLO 205, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.596×** | -8.4 | 2e-15 | 23/30 (A498, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.595×** | -8.1 | 2e-14 | 21/30 (SW 1088, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.625×** | -7.4 | 8e-12 | 17/27 (A498, hTERT-HPNE, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **0.644×** | -7.2 | 3e-11 | 21/30 (hTERT-HPNE, A498, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change | **0.646×** | -6.8 | 3e-10 | 17/23 (RPMI-7951, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.658×** | -6.8 | 3e-10 | 24/30 (HOP62, HS-578T, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.771×** | -6.0 | 7e-08 | 16/30 (Hs 766T, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.525×** | -5.5 | 1e-06 | 19/30 (C32, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.798×** | -5.2 | 6e-06 | 16/31 (C32, J82, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.563×** | -4.9 | 2e-05 | 18/28 (RPMI-7951, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.576×** | -4.7 | 6e-05 | 13/29 (Hs 766T, A498, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.751×** | -4.5 | 2e-04 | 15/30 (NCI-H1792, HS-578T, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.778×** | -4.1 | 9e-04 | 15/30 (HepG2/C3A, J82, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.839× | -4.0 | 0.001 | 14/30 (J82, NCI-H1792, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.804×** | -3.5 | 0.007 | 12/29 (J82, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.806×** | -3.5 | 0.008 | 11/30 (J82, LOX-IMVI, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.673×** | -3.4 | 0.012 | 8/30 (A498, J82, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.60 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7687. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 194 | 0 | 15 (12 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -20.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.350× (z -12.9) |
| [[HS-578T (line)]] | alt | 107 | 0 | 12 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -23.1) |
| [[hTERT-HPNE (line)]] | wt | 160 | 0 | 12 (11 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.356× (z -13.6) |
| [[NCI-H1792 (line)]] | alt | 241 | 0 | 12 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -16.0) |
| [[SW 900 (line)]] | alt | 103 | 0 | 12 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.1000× (z -19.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.223× (z -19.0) |
| [[SNU-423 (line)]] | alt | 205 | 0 | 11 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -17.9) |
| [[H4 (line)]] | wt | 115 | 0 | 10 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.107× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.253× (z -10.0) |
| [[Hs 766T (line)]] | wt | 159 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -20.8) |
| [[COLO 205 (line)]] | alt | 130 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0682× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.285× (z -11.8) |
| [[HOP62 (line)]] | alt | 41.7 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.299× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.322× (z -9.9) |
| [[J82 (line)]] | alt | 152 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.421× (z -12.7) |
| [[SHP-77 (line)]] | alt | 62.4 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -10.5) |
| [[A-172 (line)]] | wt | 138 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.198× (z -16.5) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.493× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 69.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -21.4) |
| [[C32 (line)]] | wt | 72.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change |
| [[RPMI-7951 (line)]] | alt | 63.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0477× (z -23.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change |
| [[SW480 (line)]] | alt | 22.3 | 1 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +9.7) ⚠ cell-cycle shift, explains ~34% of this change | [[Lonafarnib (drug)]] 5 µM 0.126× (z -9.0) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 27.6 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.186× (z -13.8) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.343× (z -12.4) |
| [[SW 1088 (line)]] | alt | 130 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0266× (z -14.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[AN3 CA (line)]] | alt | 42.8 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0789× (z -10.4) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 38.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.214× (z -10.3) ⚠ toxic; cell-cycle shift, explains ~36% of this change |
| [[A-427 (line)]] | wt | 7.93 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.98 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.88 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.21 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.52 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.38 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.60 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 61.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.29 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.93 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.21 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 5.18 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.23 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.62 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.80 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.18 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.77 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.50 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7687), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTGFR]] | +0.62 | +0.55 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[ATP8B2]] | +0.58 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[C9]] | +0.55 | +0.64 / +0.55 | both halves | 1e-05 | ⚠ **readthrough risk**: C9 lies 0.4 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[GLIS1]] | +0.53 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[SEMA6D]] | +0.52 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[APBB1IP]] | +0.52 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[TMOD1]] | +0.51 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[GPR173]] | +0.50 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[GSDME]] | +0.50 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[PRR16]] | +0.50 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[LOX]] | +0.49 | +0.49 / +0.44 | both halves | 3e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[HEG1]] | +0.49 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[ADAMTS2]] | +0.48 | +0.43 / +0.44 | both halves | 4e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC12A2-DT]] | -0.47 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[ANK3]] | -0.44 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[DCPS]] | -0.43 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[DLEU1]] | -0.43 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[PATJ]] | -0.42 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[STX18-AS1]] | -0.41 | -0.41 / -0.36 | both halves | 9e-05 |  |
| [[MGMT]] | -0.41 | -0.40 / -0.40 | both halves | 5e-05 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[PRKAR1B]] | -0.39 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[TESMIN]] | -0.38 | -0.42 / -0.28 | both halves | 3e-04 |  |
| [[DENND1A]] | -0.38 | -0.35 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 6, C 11. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBN1]] | B | FBN1 activity raises DAB2's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 3.57× lower at baseline in the lines without FBN1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241 |
| [[LINC01411]] | B | LINC01411 activity raises DAB2's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 6.29× lower at baseline in the lines without LINC01411 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032 |
| [[FBN1]] | B | FBN1 activity strengthens DAB2's drug response | lines that do not express FBN1 (14) vs lines expressing it (16) | the lines without FBN1 respond 0.54× as strongly (z diff +2.83); strongest at Panobinostat 5 µM: 0.58x vs 0.29x (z diff +5.0) | 0.069 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241; target measured in part of the lines; artifact flags |
| [[RARB]] | B | RARB activity raises DAB2's level | lines that do not express RARB (28) vs lines expressing it (22) | 3.13× lower at baseline in the lines without RARB | 0.087 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, NEFM, PAPPA |
| [[TNS1]] | B | TNS1 activity raises DAB2's level | lines that do not express TNS1 (23) vs lines expressing it (27) | 2.79× lower at baseline in the lines without TNS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: C5orf46, LINC02970, ENSG00000223786 |
| [[HTR1F]] | B | HTR1F activity raises DAB2's level | lines that do not express HTR1F (34) vs lines expressing it (16) | 3.48× lower at baseline in the lines without HTR1F | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MGP, TIMP3, AEBP1; maybe low, not absent |
| [[C9]] | C | C9 activity raises DAB2's level | lines that do not express C9 (21) vs lines expressing it (29) | 9.70× lower at baseline in the lines without C9 | 1e-05 | ⚠ within organs, on part of the lines; also absent: DAB2, ENSG00000253891, PTGFR; co-absent with the target |
| [[COL5A1]] | C | COL5A1 activity raises DAB2's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 5.63× lower at baseline in the lines without COL5A1 | 0.011 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; co-absent with the target |
| [[GPR173]] | C | GPR173 activity raises DAB2's level | lines that do not express GPR173 (30) vs lines expressing it (20) | 3.68× lower at baseline in the lines without GPR173 | 0.028 | ⚠ within organs, on part of the lines; also absent: ITGA11, LUM, IRAG2; co-absent with the target |
| [[LOX]] | C | LOX activity raises DAB2's level | lines that do not express LOX (31) vs lines expressing it (19) | 5.49× lower at baseline in the lines without LOX | 0.034 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411; co-absent with the target |
| [[PTGFR]] | C | PTGFR activity raises DAB2's level | lines that do not express PTGFR (28) vs lines expressing it (22) | 5.48× lower at baseline in the lines without PTGFR | 0.034 | ⚠ within organs, on part of the lines; also absent: ITGA4, FRMD4A, LOX; co-absent with the target |
| [[KC6]] | C | KC6 activity raises DAB2's level | lines that do not express KC6 (32) vs lines expressing it (18) | 4.58× lower at baseline in the lines without KC6 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, CCNYL2, COL19A1; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 8, C 12. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNS1]] | B | DAB2 activity raises TNS1's level | lines that do not express DAB2 (18) vs lines expressing it (32) | 3.82× lower at baseline in the lines without DAB2 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: C9, NNMT, DPYSL3 |
| [[NAGK]] | B | DAB2 activity raises NAGK's level | lines that do not express DAB2 (18) vs lines expressing it (32) | 1.45× lower at baseline in the lines without DAB2 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: C9, NNMT, DPYSL3 |
| [[RARB]] | B | DAB2 activity raises RARB's level | lines that do not express DAB2 (18) vs lines expressing it (32) | 3.51× lower at baseline in the lines without DAB2 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: C9, NNMT, DPYSL3 |
| [[TMEM92-AS1]] | B | DAB2 activity raises TMEM92-AS1's level | lines that do not express DAB2 (18) vs lines expressing it (32) | 2.25× lower at baseline in the lines without DAB2 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: C9, NNMT, DPYSL3 |
| [[GSDME]] | B | DAB2 activity strengthens GSDME's drug response | lines that do not express DAB2 (8) vs lines expressing it (25) | the lines without DAB2 respond 0.55× as strongly (z diff +2.54); strongest at Panobinostat 0.5 µM: 0.72x vs 0.29x (z diff +5.4) | 0.076 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: C9, NNMT, DPYSL3; target measured in part of the lines; artifact flags |
| [[MACO1]] | B | DAB2 activity raises MACO1's level | lines that do not express DAB2 (18) vs lines expressing it (32) | 1.32× lower at baseline in the lines without DAB2 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: C9, NNMT, DPYSL3 |
| [[GSDME]] | B | DAB2 activity raises GSDME's level | lines that do not express DAB2 (18) vs lines expressing it (32) | 3.45× lower at baseline in the lines without DAB2 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: C9, NNMT, DPYSL3 |
| [[ATOSB]] | B | DAB2 activity raises ATOSB's level | lines that do not express DAB2 (18) vs lines expressing it (32) | 1.81× lower at baseline in the lines without DAB2 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: C9, NNMT, DPYSL3 |
| [[C9]] | C | DAB2 activity raises C9's level | lines that do not express DAB2 (18) vs lines expressing it (32) | 3.80× lower at baseline in the lines without DAB2 | 8e-04 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: C9, NNMT, DPYSL3; co-absent with the target |
| [[LOX]] | C | DAB2 activity raises LOX's level | lines that do not express DAB2 (18) vs lines expressing it (32) | 6.34× lower at baseline in the lines without DAB2 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: C9, NNMT, DPYSL3; co-absent with the target |
| [[BICC1]] | C | DAB2 activity raises BICC1's level | lines that do not express DAB2 (18) vs lines expressing it (32) | 4.42× lower at baseline in the lines without DAB2 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: C9, NNMT, DPYSL3; co-absent with the target |
| [[MSC-AS1]] | C | DAB2 activity raises MSC-AS1's level | lines that do not express DAB2 (18) vs lines expressing it (32) | 5.78× lower at baseline in the lines without DAB2 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: C9, NNMT, DPYSL3; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.419). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (58.2, 16.5); signed map (27.8, 44.6). **Vector** length 101, 27.2% of its response variance represented; |z| ≥ 3 in 1,071 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +7.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +5.9 | +6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change | +4.5 | -6.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.1 | +1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | -0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +1.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | +4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +1.1 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -6.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.0 | -8.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -2.0 | -9.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | -1.8 | -4.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.7 | -4.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | +0.8 |
|  | [[Encorafenib (drug)]] 5 µM |  | -1.5 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | DAB adaptor protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.1 — chr5:39,371,675-39,462,300 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DOC-2 |
| Hallmark sets | UV_RESPONSE_DN, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 8 pathways, smallest: Formation of annular gap junctions; Gap junction degradation; Gap junction trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [P98082](https://www.uniprot.org/uniprotkb/P98082) (Disabled homolog 2):

> Adapter protein that functions as a clathrin-associated sorting protein (CLASP) required for clathrin-mediated endocytosis of selected cargo proteins. Can bind and assemble clathrin, and binds simultaneously to phosphatidylinositol 4,5-bisphosphate (PtdIns(4,5)P2) and cargos containing non-phosphorylated NPXY internalization motifs, such as the LDL receptor, to recruit them to clathrin-coated pits. Can function in clathrin-mediated endocytosis independently of the AP-2 complex. Involved in …

**Summary**, from NCBI Gene [1601](https://www.ncbi.nlm.nih.gov/gene/1601):

> This gene encodes a mitogen-responsive phosphoprotein. It is expressed in normal ovarian epithelial cells, but is down-regulated or absent from ovarian carcinoma cell lines, suggesting its role as a tumor suppressor. This protein binds to the SH3 domains of GRB2, an adaptor protein that couples tyrosine kinase receptors to SOS (a guanine nucleotide exchange factor for Ras), via its C-terminal proline-rich sequences, and may thus modulate growth factor/Ras pathways by competing with SOS for …

**Accessions** — [HGNC:2662](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2662) · Entrez [1601](https://www.ncbi.nlm.nih.gov/gene/1601) · UniProt [P98082](https://www.uniprot.org/uniprotkb/P98082) · Ensembl [ENSG00000153071](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153071)

## Data

Gene col 7687: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7687); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7687, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7687]; `tensor/DDL_lfc|DDL_z.npy` [7687]; `embed/gene_vectors.npy` [7687]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7687 or target_col == 7687). Every well: [[DAB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DAB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
