---
symbol: "IFI44"
type: "gene"
col: 6102
ensembl_id: "ENSG00000137965"
name: "interferon induced protein 44"
location: "1p31.1"
module: 32
arm: "+"
pooled_cpm: 79.76
n_lines_expressing: 38
n_dd_up: 19
n_dd_down: 65
n_dd_up_clean: 18
n_dd_down_clean: 50
in_vector_space: true
direction_upstream: 68
direction_downstream: 93
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# IFI44

*interferon induced protein 44* — 1p31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.78× (z +6.9, q 3e-09, up in 28 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 65 drug-doses (15 with an alert ⚠); the strongest is [[Tofacitinib (drug)]] 5 µM: 0.317× (z -20.0, q 0e+00, down in 28 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OAS1]] (+0.94, fdr 7e-06), [[IFI44L]] (+0.93, fdr 7e-06, ⚠ same locus), [[MX1]] (+0.93, fdr 7e-06), [[CMPK2]] (+0.93, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 68 arrows point to it, the strongest [[PLAAT4]] → it (grade B ⚠); 93 go from it, the strongest it → [[OAS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6102.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.78×** | +6.9 | 3e-09 | 28/35 (LoVo, AsPC-1, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.62×** | +5.8 | 2e-06 | 27/36 (LoVo, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.48×** | +4.8 | 3e-04 | 24/37 (LoVo, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.46×** | +4.7 | 4e-04 | 23/35 (LoVo, Hs 766T, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.45×** | +4.6 | 4e-04 | 23/36 (NCI-H460, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.32×** | +4.4 | 0.001 | 22/36 (Hs 766T, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.32×** | +4.3 | 0.001 | 21/36 (AsPC-1, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +4.3 | 0.001 | 21/36 (NCI-H2347, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.26×** | +4.0 | 0.005 | 22/37 (Hs 766T, LoVo, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.36×** | +3.8 | 0.009 | 22/37 (LoVo, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.27×** | +3.6 | 0.014 | 20/38 (AsPC-1, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[venetoclax (drug)]] 0.05 µM |  | **1.36×** | +3.6 | 0.017 | 18/37 (LoVo, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **1.23×** | +3.5 | 0.017 | 22/36 (Hs 766T, LoVo, …) | all doses, flat |  |
| [[Larotrectinib (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.034 | 13/36 (CFPAC-1, SW1417, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.30×** | +3.2 | 0.046 | 12/36 (Panc 03.27, A-172, …) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.31×** | +3.2 | 0.057 | 15/36 (Hs 766T, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 66 in all, 15 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 65 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6102.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | **0.317×** | -20.0 | 0e+00 | 28/37 (RPMI-7951, NCI-H1792, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.228×** | -18.2 | 0e+00 | 34/36 (LoVo, SNU-423, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.232×** | -18.0 | 0e+00 | 34/36 (RPMI-7951, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.240×** | -17.5 | 0e+00 | 35/36 (RPMI-7951, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.388×** | -16.5 | 0e+00 | 28/37 (RPMI-7951, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.277×** | -15.8 | 0e+00 | 32/37 (SNU-423, RPMI-7951, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.435×** | -14.5 | 1e-45 | 29/36 (NCI-H1573, LoVo, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.315×** | -14.2 | 5e-44 | 34/36 (BT-474, RPMI-7951, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.329×** | -13.7 | 1e-40 | 28/36 (LoVo, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.509×** | -11.7 | 6e-30 | 34/37 (BT-474, A-172, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.392×** | -11.5 | 6e-29 | 27/37 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.441×** | -10.1 | 4e-22 | 32/36 (LoVo, SNU-423, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.452×** | -9.8 | 7e-21 | 31/36 (SNU-423, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.611×** | -8.6 | 5e-16 | 33/37 (A-172, CFPAC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.516×** | -7.8 | 2e-13 | 27/35 (NCI-H1792, A498, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.315×** | -7.4 | 4e-12 | 30/37 (RPMI-7951, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6102. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 116 | 0 | 25 (9 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0391× (z -21.3) |
| [[NCI-H1573 (line)]] | alt | 117 | 0 | 23 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0879× (z -27.2) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0734× (z -20.7) |
| [[BT-474 (line)]] | alt | 64.8 | 0 | 21 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0161× (z -24.8) |
| [[NCI-H1792 (line)]] | alt | 174 | 0 | 21 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -22.2) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.217× (z -19.1) |
| [[RPMI-7951 (line)]] | alt | 334 | 0 | 18 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.110× (z -22.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.136× (z -21.0) |
| [[SNU-423 (line)]] | alt | 61.2 | 0 | 17 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0581× (z -20.4) |
| [[A498 (line)]] | wt | 150 | 0 | 16 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -17.8) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.237× (z -16.4) |
| [[HS-578T (line)]] | alt | 108 | 0 | 16 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0895× (z -19.5) |
| [[RKO (line)]] | wt | 56.7 | 0 | 15 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0361× (z -15.0) |
| [[KATO III (line)]] | alt | 68.4 | 0 | 14 (3 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.163× (z -17.3) |
| [[A549 (line)]] | wt | 35.6 | 0 | 13 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0590× (z -16.7) |
| [[AsPC-1 (line)]] | alt | 79.2 | 0 | 13 (2 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.215× (z -15.4) |
| [[A-172 (line)]] | wt | 158 | 0 | 12 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.163× (z -15.6) |
| [[CFPAC-1 (line)]] | alt | 171 | 0 | 12 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.127× (z -19.5) ⚠ toxic · without an alert: [[Tofacitinib (drug)]] 5 µM 0.257× (z -18.9) |
| [[NCI-H460 (line)]] | wt | 157 | 9 (7 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +17.6) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.19× (z +13.2) | [[Panobinostat (drug)]] 5 µM 0.407× (z -10.1) |
| [[Panc 03.27 (line)]] | alt | 229 | 0 | 12 | — | [[Tofacitinib (drug)]] 5 µM 0.262× (z -16.4) |
| [[NCI-H2347 (line)]] | alt | 95.8 | 1 | 10 | [[Harringtonine (drug)]] 0.5 µM 2.67× (z +8.8) | [[Tofacitinib (drug)]] 5 µM 0.225× (z -18.8) |
| [[Hs 766T (line)]] | wt | 235 | 0 | 10 | — | [[Tofacitinib (drug)]] 5 µM 0.347× (z -12.4) |
| [[SHP-77 (line)]] | alt | 35.9 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -12.0) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.203× (z -10.7) |
| [[LS 180 (line)]] | wt | 82.9 | 4 (4 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +15.5) ⚠ cell-cycle shift, explains ~47% of this change | [[Panobinostat (drug)]] 0.5 µM 0.230× (z -11.8) |
| [[COLO 205 (line)]] | alt | 46.0 | 0 | 6 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0806× (z -11.0) |
| [[LOX-IMVI (line)]] | wt | 112 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -13.1) |
| [[HEC-1-A (line)]] | alt | 21.3 | 2 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +12.0) ⚠ cell-cycle shift, explains ~47% of this change | [[Panobinostat (drug)]] 5 µM 0.194× (z -10.4) |
| [[SW1417 (line)]] | alt | 40.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -9.2) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.244× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 65.4 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +8.9) ⚠ cell-cycle shift, explains ~47% of this change | [[Panobinostat (drug)]] 5 µM 0.282× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 83.0 | 0 | 3 | — | [[Tofacitinib (citrate) (drug)]] 5 µM 0.240× (z -13.0) |
| [[C32 (line)]] | wt | 48.2 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 4.49× (z +9.5) | — |
| [[J82 (line)]] | alt | 83.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.78× (z +10.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 51.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +21.0) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[NCI-H23 (line)]] | alt | 22.4 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0722× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.183× (z -10.8) |
| [[CHP-212 (line)]] | wt | 58.7 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0880× (z -8.9) |
| [[H4 (line)]] | wt | 83.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.190× (z -10.4) ⚠ toxic |
| [[SW 900 (line)]] | alt | 105 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.269× (z -9.3) |
| [[A-427 (line)]] | wt | 5.26 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 12.9 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 9.83 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 16.9 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 11.9 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 14.6 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 95.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 70.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.7 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 7.33 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 11.2 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 88.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.79 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.10 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6102), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OAS1]] | +0.94 | +0.87 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 961 |
| [[IFI44L]] | +0.93 | +0.87 / +0.96 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 999; ⚠ same locus (3.7 kb, same strand: neighbours can correlate without regulation) |
| [[MX1]] | +0.93 | +0.89 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 967 |
| [[CMPK2]] | +0.93 | +0.89 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 790 |
| [[RSAD2]] | +0.93 | +0.91 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 983 |
| [[OAS2]] | +0.93 | +0.88 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 941 |
| [[PARP9]] | +0.92 | +0.87 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 929 |
| [[IFIT1]] | +0.92 | +0.88 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 974 |
| [[MX2]] | +0.91 | +0.86 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 872 |
| [[XAF1]] | +0.91 | +0.82 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 970 |
| [[IFI35]] | +0.91 | +0.85 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 924 |
| [[IFIT3]] | +0.91 | +0.88 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 984 |
| [[HERC6]] | +0.90 | +0.88 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 908 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*68 arrows, 68 of them with an alert ⚠; grade A 0, B 50, C 18. Shown: the 12 strongest; 56 more arrows (56 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLAAT4]] | B | PLAAT4 activity raises IFI44's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 3.20× lower at baseline in the lines without PLAAT4 | 6e-04 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[IFIT3]] | B | IFIT3 activity raises IFI44's level | lines that do not express IFIT3 (8) vs lines expressing it (42) | 5.39× lower at baseline in the lines without IFIT3 | 0.001 | ⚠ within organs, on part of the lines; also absent: GBP2, IFIT2, TRIM38; maybe low, not absent |
| [[EPSTI1]] | B | EPSTI1 activity raises IFI44's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 3.36× lower at baseline in the lines without EPSTI1 | 0.001 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[OASL]] | B | OASL activity raises IFI44's level | lines that do not express OASL (10) vs lines expressing it (40) | 4.19× lower at baseline in the lines without OASL | 0.002 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |
| [[CASP10]] | B | CASP10 activity raises IFI44's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 2.39× lower at baseline in the lines without CASP10 | 0.003 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[OAS2]] | B | OAS2 activity strengthens IFI44's drug response | lines that do not express OAS2 (5) vs lines expressing it (32) | the lines without OAS2 respond 0.34× as strongly (z diff +3.88); strongest at Fedratinib (hydrochloride hydrate) 5 µM: 0.64x vs 0.23x (z diff +5.1) | 0.003 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1; target measured in part of the lines; artifact flags |
| [[MX1]] | B | MX1 activity raises IFI44's level | lines that do not express MX1 (19) vs lines expressing it (31) | 2.77× lower at baseline in the lines without MX1 | 0.004 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[NLRC5]] | B | NLRC5 activity raises IFI44's level | lines that do not express NLRC5 (5) vs lines expressing it (45) | 4.62× lower at baseline in the lines without NLRC5 | 0.004 | ⚠ within organs, on part of the lines; also absent: NDRG1, APOL6, S100A13; maybe low, not absent |
| [[CTSS]] | B | CTSS activity raises IFI44's level | lines that do not express CTSS (15) vs lines expressing it (35) | 3.26× lower at baseline in the lines without CTSS | 0.004 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[HERC6]] | B | HERC6 activity raises IFI44's level | lines that do not express HERC6 (5) vs lines expressing it (45) | 5.04× lower at baseline in the lines without HERC6 | 0.007 | ⚠ within organs, on part of the lines; also absent: IFIH1, IFI35, PARP9; maybe low, not absent |
| [[GBP4]] | B | GBP4 activity raises IFI44's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 3.68× lower at baseline in the lines without GBP4 | 0.007 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[OAS1]] | B | OAS1 activity raises IFI44's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 3.10× lower at baseline in the lines without OAS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |

### Downstream of this gene

*93 arrows, 93 of them with an alert ⚠; grade A 0, B 84, C 9. Shown: the 12 strongest; 81 more arrows (81 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OAS1]] | B | IFI44 activity raises OAS1's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 3.20× lower at baseline in the lines without IFI44 | 0.001 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[PLSCR1]] | B | IFI44 activity raises PLSCR1's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 2.81× lower at baseline in the lines without IFI44 | 0.001 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[APOL6]] | B | IFI44 activity raises APOL6's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 2.53× lower at baseline in the lines without IFI44 | 0.001 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[NLRC5]] | B | IFI44 activity raises NLRC5's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 2.19× lower at baseline in the lines without IFI44 | 0.003 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[B2M]] | B | IFI44 activity raises B2M's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 2.09× lower at baseline in the lines without IFI44 | 0.003 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[DDX60L]] | B | IFI44 activity raises DDX60L's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 3.34× lower at baseline in the lines without IFI44 | 0.003 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[ISG20]] | B | IFI44 activity raises ISG20's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 2.36× lower at baseline in the lines without IFI44 | 0.003 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[HERC6]] | B | IFI44 activity raises HERC6's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 2.50× lower at baseline in the lines without IFI44 | 0.003 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[MYD88]] | B | IFI44 activity raises MYD88's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 1.84× lower at baseline in the lines without IFI44 | 0.004 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[GBP3]] | B | IFI44 activity raises GBP3's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 3.53× lower at baseline in the lines without IFI44 | 0.005 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[RIGI]] | B | IFI44 activity raises RIGI's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 1.81× lower at baseline in the lines without IFI44 | 0.006 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[PARP14]] | B | IFI44 activity raises PARP14's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 2.04× lower at baseline in the lines without IFI44 | 0.006 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.951). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.6, 53.7); signed map (64.9, 31.5). **Vector** length 158, 60.6% of its response variance represented; |z| ≥ 3 in 1,644 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interferon alpha/beta signaling* (reactome, mean cos +0.85 to 27); *Interferon gamma signaling* (reactome, mean cos +0.79 to 17); *Antimicrobial mechanism of IFN-stimulated genes* (reactome, mean cos +0.85 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.3 | +1.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +8.0 | +4.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +6.9 | +6.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.8 | +0.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +5.6 | -3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.8 | +0.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.4 | +4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.4 | +5.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.3 | +4.3 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -11.2 | -20.0 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -9.4 | -16.5 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -9.2 | -11.5 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -8.7 | -13.7 |
|  | [[Selinexor (drug)]] 5 µM |  | -8.5 | -14.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -7.6 | -15.8 |

## What is on record

|  |  |
|---|---|
| Name | interferon induced protein 44 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.1 — chr1:78,649,796-78,664,078 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MTAP44, p44, TLDC5 |
| Gene groups (HGNC) | TLDc domain containing |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INTERFERON_GAMMA_RESPONSE |
| Reactome | 3 pathways, smallest: Modulation of host responses by IFN-stimulated genes; Interferon Signaling; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TCB0](https://www.uniprot.org/uniprotkb/Q8TCB0) (Interferon-induced protein 44):

> This protein aggregates to form microtubular structures.

**Summary**, from NCBI Gene [10561](https://www.ncbi.nlm.nih.gov/gene/10561):

> Predicted to be involved in immune response. Predicted to act upstream of or within cellular response to virus and response to bacterium. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16938](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16938) · Entrez [10561](https://www.ncbi.nlm.nih.gov/gene/10561) · UniProt [Q8TCB0](https://www.uniprot.org/uniprotkb/Q8TCB0) · Ensembl [ENSG00000137965](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137965)

## Data

Gene col 6102: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6102); `tables/drug_effects.parquet` (86 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6102, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6102]; `tensor/DDL_lfc|DDL_z.npy` [6102]; `embed/gene_vectors.npy` [6102]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6102 or target_col == 6102). Every well: [[IFI44 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IFI44.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
