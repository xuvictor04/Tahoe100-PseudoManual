---
symbol: "ARMCX5-GPRASP2"
type: "gene"
col: 15677
ensembl_id: "ENSG00000271147"
name: "ARMCX5-GPRASP2 readthrough"
location: "Xq22.1"
module: 23
arm: "+"
pooled_cpm: 23.72
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 10
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# ARMCX5-GPRASP2

*ARMCX5-GPRASP2 readthrough* — Xq22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.78× (z +11.6, q 3e-28, up in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.60× (z +6.7, q 5e-09, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.589× (z -7.5, q 2e-11, down in 32 of 48 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Peretinoin (drug)]] 5 µM: 0.753× (z -3.9, q 0.009, down in 18 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (KATO III 0.185×, HEC-1-A 0.280×, HCT15 0.149×, C32 0.271×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (HS-578T 0.0564×, H4 0.0822×; ⚠ toxic; cell-cycle shift, explains ~53% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (Hs 766T 0.0802×, RPMI-7951 0.120×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (C32 0.386×, NCI-H1792 0.316×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0914×); [[Hesperidin (drug)]] 5 µM in 1 line (hTERT-HPNE 0.162×).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPRASP1]] (+0.81, fdr 7e-06, ⚠ read-through risk), [[GPRASP3]] (+0.75, fdr 7e-06, ⚠ same locus), [[RRAGB]] (+0.70, fdr 7e-06), [[ZNF91]] (+0.70, fdr 1e-05), [[GTF2H1]] (+0.68, fdr 2e-05); moves opposite to [[DHTKD1]] (-0.62, fdr 9e-05), [[DNAAF3]] (-0.61, fdr 4e-04), [[EHD4]] (-0.60, fdr 6e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LINC00665]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15677.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.78×** | +11.6 | 3e-28 | 43/48 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +6.7 | 5e-09 | 31/48 (SNU-423, PANC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +6.3 | 4e-08 | 28/47 (NCI-H2347, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.56×** | +6.3 | 4e-08 | 29/48 (NCI-H2347, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.51×** | +5.9 | 4e-07 | 25/47 (NCI-H2030, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.43×** | +5.1 | 3e-05 | 25/48 (MIA PaCa-2, J82, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +4.1 | 0.003 | 21/47 (SW480, NCI-H23, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.34×** | +3.8 | 0.010 | 10/48 (SW480, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.20×** | +3.6 | 0.019 | 15/48 (Hs 766T, SW480, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.042 | 13/48 (HEC-1-A, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.072 | 15/47 (NCI-H23, SW480, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.27×** | +3.1 | 0.080 | 14/48 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +3.1 | 0.081 | 8/48 (C32, NCI-H460, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.16× | +3.1 | 0.081 | 6/48 (KATO III, J82, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.51×** | +3.1 | 0.081 | 4/48 (HEC-1-A, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.24×** | +3.0 | 0.081 | 7/48 (MIA PaCa-2, KATO III, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.16× | +3.0 | 0.081 | 9/48 (LS 180, HT-29, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.0 | 0.081 | 17/46 (HS-578T, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15677.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (KATO III 0.185×, HEC-1-A 0.280×, HCT15 0.149×, C32 0.271×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (HS-578T 0.0564×, H4 0.0822×; ⚠ toxic; cell-cycle shift, explains ~53% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (Hs 766T 0.0802×, RPMI-7951 0.120×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (C32 0.386×, NCI-H1792 0.316×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0914×); [[Hesperidin (drug)]] 5 µM in 1 line (hTERT-HPNE 0.162×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.589×** | -7.5 | 2e-11 | 32/48 (COLO 205, SW480, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.590×** | -7.5 | 2e-11 | 35/48 (SW480, HCT15, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **0.599×** | -7.3 | 7e-11 | 28/43 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.620×** | -6.8 | 2e-09 | 30/48 (SW480, HCT15, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change | **0.697×** | -4.9 | 1e-04 | 17/32 (C32, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~53% of this change | **0.701×** | -4.8 | 1e-04 | 25/47 (HS-578T, H4, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.753×** | -3.9 | 0.009 | 18/47 (H4, NCI-H2347, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.773×** | -3.6 | 0.020 | 17/47 (HEC-1-A, H4, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.780×** | -3.5 | 0.026 | 15/48 (CFPAC-1, RPMI-7951, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.839× | -3.5 | 0.026 | 15/48 (C32, C-33 A, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.796×** | -3.2 | 0.065 | 16/47 (SW480, A-172, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15677. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 47.3 | 0 | 7 (7 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.318× (z -10.3) ⚠ cell-cycle shift, explains ~42% of this change |
| [[C32 (line)]] | wt | 46.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.214× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.386× (z -10.1) |
| [[A498 (line)]] | wt | 8.14 | 1 (1 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 3.33× (z +9.6) ⚠ cell-cycle shift, explains ~37% of this change | [[Digitoxin (drug)]] 5 µM 0.226× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 15.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +9.2) | — |
| [[J82 (line)]] | alt | 13.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +11.4) | — |
| [[NCI-H2030 (line)]] | alt | 12.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.203× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change |
| [[NCI-H2347 (line)]] | alt | 9.17 | 2 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 4.69× (z +13.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 4.12× (z +11.9) | — |
| [[A-172 (line)]] | wt | 8.62 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.144× (z -9.3) |
| [[A549 (line)]] | wt | 20.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.227× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change |
| [[AN3 CA (line)]] | alt | 24.1 | 0 | 1 | — | [[Loperamide (hydrochloride) (drug)]] 0.05 µM 0.0755× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 15.8 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.60× (z +8.9) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[COLO 205 (line)]] | alt | 28.9 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0854× (z -14.5) ⚠ cell-cycle shift, explains ~37% of this change |
| [[H4 (line)]] | wt | 53.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0822× (z -14.0) ⚠ toxic; cell-cycle shift, explains ~53% of this change |
| [[HCT15 (line)]] | alt | 32.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[HEC-1-A (line)]] | alt | 36.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[HepG2_C3A (line)]] | wt | 21.3 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0914× (z -10.8) |
| [[Hs 766T (line)]] | wt | 21.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0802× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0564× (z -15.6) ⚠ toxic; cell-cycle shift, explains ~53% of this change |
| [[hTERT-HPNE (line)]] | wt | 26.9 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.162× (z -10.3) |
| [[KATO III (line)]] | alt | 45.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[NCI-H1573 (line)]] | alt | 31.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.234× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change |
| [[NCI-H1792 (line)]] | alt | 16.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 39.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 30.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.120× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 20.3 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.99× (z +9.9) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[A-427 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15677), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 11 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPRASP1]] | +0.81 | +0.80 / +0.72 | both halves | 7e-06 | ⚠ **readthrough risk**: GPRASP1 lies 0.0 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[GPRASP3]] | +0.75 | +0.77 / +0.69 | both halves | 7e-06 | ⚠ same locus (6.0 kb, same strand: neighbours can correlate without regulation) |
| [[RRAGB]] | +0.70 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[ZNF91]] | +0.70 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[GTF2H1]] | +0.68 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[OXA1L-DT]] | +0.67 | +0.66 / +0.38 | both halves | 6e-05 |  |
| [[THBS4]] | +0.67 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[POLR2M]] | +0.66 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[YAE1]] | +0.66 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[THAP2]] | +0.66 | +0.64 / +0.32 | both halves | 2e-04 |  |
| [[AEBP2]] | +0.65 | +0.62 / +0.34 | both halves | 1e-04 |  |
| [[TAS2R4]] | +0.65 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[MCPH1]] | +0.65 | +0.57 / +0.34 | both halves | 1e-04 |  |
| [[MFF-DT]] | +0.64 | +0.64 / +0.22 | both halves | 6e-04 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHTKD1]] | -0.62 | -0.42 / -0.37 | both halves | 9e-05 |  |
| [[DNAAF3]] | -0.61 | -0.30 / -0.26 | both halves | 4e-04 |  |
| [[EHD4]] | -0.60 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[GRK6]] | -0.59 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[TECPR1]] | -0.58 | -0.29 / -0.31 | both halves | 2e-04 |  |
| [[TNK2]] | -0.58 | -0.57 / -0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[MAPKAPK2]] | -0.57 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[NUP93]] | -0.57 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[FLNB]] | -0.57 | -0.58 / -0.25 | both halves | 4e-04 |  |
| [[TSEN54]] | -0.57 | -0.44 / -0.30 | both halves | 2e-04 |  |
| [[CORO2A]] | -0.57 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[CARHSP1]] | -0.57 | -0.49 / -0.26 | both halves | 4e-04 |  |
| [[GNA12]] | -0.57 | -0.56 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00665]] | B | LINC00665 activity raises ARMCX5-GPRASP2's level | lines that do not express LINC00665 (13) vs lines expressing it (37) | 1.34× lower at baseline in the lines without LINC00665 | 0.059 | ⚠ within organs, on part of the lines; also absent: ANKRD6, PPM1E, ZNF518B |
| [[LINC01748]] | B | LINC01748 activity raises ARMCX5-GPRASP2's level | lines that do not express LINC01748 (34) vs lines expressing it (16) | 1.35× lower at baseline in the lines without LINC01748 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CALB1, ATP10B, CLRN3 |
| [[HDAC6]] | B | HDAC6 activity raises ARMCX5-GPRASP2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[RAPGEF4]] | B | RAPGEF4 activity raises ARMCX5-GPRASP2's level | lines that do not express RAPGEF4 (5) vs lines expressing it (45) | 1.43× lower at baseline in the lines without RAPGEF4 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000286739, BIVM, CLIP3; maybe low, not absent |
| [[TNNI3K]] | C | TNNI3K activity weakens ARMCX5-GPRASP2's drug response | lines that do not express TNNI3K (3) vs lines expressing it (45) | the lines without TNNI3K respond 1.31× as strongly (z diff -0.70); strongest at Homoharringtonine 5 µM: 2.97x vs 1.30x (z diff -6.3) | 0.057 | ⚠ few lines (3 vs 47); across organs; also absent: CORIN, CLEC2D, CFAP58; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.702). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-2.4, 17.3); signed map (16.7, -14.2). **Vector** length 95.7, 21.5% of its response variance represented; |z| ≥ 3 in 1,022 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +11.3 | +11.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.8 | +6.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +6.0 | +6.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.6 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.7 | +5.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.0 | +5.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +0.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +4.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.5 | +1.2 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -6.5 | -7.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -6.2 | -7.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -6.1 | -6.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -4.1 | -3.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.6 | -1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.6 | -3.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -2.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -1.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.4 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | ARMCX5-GPRASP2 readthrough |
| Locus type | readthrough (other) |
| Location | Xq22.1 — chrX:102,599,512-102,714,671 (+) |
| Ensembl biotype | lncRNA |
| Matched by | symbol |

**Summary**, from NCBI Gene [100528062](https://www.ncbi.nlm.nih.gov/gene/100528062):

> This locus represents naturally occurring readthrough transcription among the adjacent armadillo repeat containing, X-linked 5 (ARMCX5), G protein-coupled receptor associated sorting proteins 1 and 2 (GPRASP1 and GPRASP2), basic helix-loop-helix family member b9 (BHLHB9), and long intergenic non-protein coding RNA 630 (LINC00630) genes on chromosome X. Transcripts may make use of multiple alternative promoters and polyadenylation signals in this region. Readthrough transcripts may produce …

**Accessions** — [HGNC:42000](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:42000) · Entrez [100528062](https://www.ncbi.nlm.nih.gov/gene/100528062) · Ensembl [ENSG00000271147](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000271147)

## Data

Gene col 15677: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15677); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15677, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15677]; `tensor/DDL_lfc|DDL_z.npy` [15677]; `embed/gene_vectors.npy` [15677]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15677 or target_col == 15677). Every well: [[ARMCX5-GPRASP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARMCX5-GPRASP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
