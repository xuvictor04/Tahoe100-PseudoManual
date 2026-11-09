---
symbol: "IMMP1L"
type: "gene"
col: 7331
ensembl_id: "ENSG00000148950"
name: "inner mitochondrial membrane peptidase subunit 1"
location: "11p13"
module: 17
arm: "+"
pooled_cpm: 65.35
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 18
n_dd_up_clean: 6
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# IMMP1L

*inner mitochondrial membrane peptidase subunit 1* — 11p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 1.46× (z +9.6, q 4e-19, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.483× (z -17.7, q 0e+00, down in 35 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.625× (z -16.8, q 0e+00, down in 42 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CENPW]] (+0.64, fdr 1e-05), [[POT1]] (+0.64, fdr 1e-05), [[LSM2]] (+0.63, fdr 1e-05); moves opposite to [[DDX5]] (-0.60, fdr 1e-05), [[LINC00393]] (-0.56, fdr 4e-05), [[CCDC200]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[COL27A1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7331.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.46×** | +9.6 | 4e-19 | 39/48 (A498, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.45×** | +9.4 | 2e-18 | 35/48 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.34×** | +7.4 | 2e-11 | 32/48 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.17× | +5.7 | 2e-06 | 19/48 (AsPC-1, HT-29, …) | rises with dose | low cells (technical?) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.14× | +4.5 | 7e-04 | 4/48 (A549, SHP-77, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.36×** | +4.0 | 0.005 | 18/49 (A-427, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.32×** | +3.7 | 0.020 | 14/47 (RKO, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.033 | 13/49 (HT-29, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 1.13× | +3.1 | 0.12 | 10/48 (COLO 205, Hs 766T, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.13× | +3.0 | 0.13 | 11/48 (RKO, hTERT-HPNE, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7331.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.483×** | -17.7 | 0e+00 | 35/42 (A-172, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.625×** | -16.8 | 0e+00 | 42/49 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.517×** | -16.7 | 0e+00 | 42/49 (NCI-H23, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.541×** | -15.6 | 0e+00 | 44/48 (SK-MEL-2, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.549×** | -14.0 | 1e-42 | 36/45 (HEC-1-A, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.676×** | -9.6 | 1e-19 | 37/50 (HEC-1-A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.717×** | -8.1 | 5e-14 | 28/48 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | **0.820×** | -7.1 | 8e-11 | 22/48 (Hs 766T, NCI-H1792, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.782×** | -6.2 | 3e-08 | 25/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.777×** | -6.2 | 4e-08 | 27/47 (SHP-77, SNU-423, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~25% of this change | **0.819×** | -5.1 | 2e-05 | 22/47 (NCI-H2347, A498, …) | inconsistent across doses | low cells (technical?) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.683×** | -5.1 | 2e-05 | 23/48 (MIA PaCa-2, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.812×** | -5.0 | 3e-05 | 23/48 (CHP-212, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.822×** | -5.0 | 3e-05 | 22/48 (NCI-H460, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.817×** | -4.9 | 3e-05 | 22/48 (NCI-H1573, PANC-1, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.887× | -4.3 | 5e-04 | 22/48 (SNU-1, A-427, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.800×** | -4.0 | 0.002 | 13/48 (PANC-1, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.05 µM |  | 0.869× | -3.4 | 0.021 | 15/48 (SHP-77, HS-578T, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.876× | -3.4 | 0.022 | 6/48 (SW480, Hs 766T, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | 0.845× | -3.0 | 0.063 | 12/48 (MIA PaCa-2, COLO 205, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7331. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 83.1 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.265× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -12.3) |
| [[HOP62 (line)]] | alt | 68.4 | 0 | 7 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.310× (z -14.1) |
| [[HEC-1-A (line)]] | alt | 87.0 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.268× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -12.7) |
| [[NCI-H2347 (line)]] | alt | 72.6 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -12.6) |
| [[NCI-H460 (line)]] | wt | 49.8 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -17.2) |
| [[PANC-1 (line)]] | alt | 61.0 | 1 (1 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.85× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.464× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.538× (z -9.0) |
| [[A-172 (line)]] | wt | 47.4 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0713× (z -26.7) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -14.9) |
| [[LOX-IMVI (line)]] | wt | 58.8 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -12.3) |
| [[RKO (line)]] | wt | 58.1 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.366× (z -9.9) |
| [[A-427 (line)]] | wt | 110 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.05 µM 0.408× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.533× (z -8.5) |
| [[A498 (line)]] | wt | 53.8 | 2 | 1 | [[Belinostat (drug)]] 5 µM 2.13× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -14.6) |
| [[C-33 A (line)]] | alt | 66.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.135× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.230× (z -13.1) |
| [[J82 (line)]] | alt | 59.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -15.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 82.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.355× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.585× (z -11.4) |
| [[NCI-H23 (line)]] | alt | 52.8 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -9.4) |
| [[SNU-1 (line)]] | wt | 64.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -15.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 98.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.377× (z -12.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 118 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.424× (z -13.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 56.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -14.0) |
| [[BT-474 (line)]] | alt | 69.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -11.0) |
| [[HepG2_C3A (line)]] | wt | 57.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -9.8) |
| [[Hs 766T (line)]] | wt | 46.0 | 0 | 2 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.416× (z -10.8) |
| [[KATO III (line)]] | alt | 40.8 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.61× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 59.5 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.235× (z -13.7) |
| [[NCI-H1792 (line)]] | alt | 44.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -19.8) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 46.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -14.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 91.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -11.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 61.2 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.217× (z -15.5) |
| [[C32 (line)]] | wt | 55.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -10.7) |
| [[CFPAC-1 (line)]] | alt | 43.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.313× (z -11.4) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 42.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.112× (z -9.7) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 83.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -9.3) |
| [[HCT15 (line)]] | alt | 110 | 0 | 1 | — | [[OTS514 (drug)]] 5 µM 0.186× (z -9.1) |
| [[LS 180 (line)]] | wt | 67.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -10.6) |
| [[Panc 03.27 (line)]] | alt | 99.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.396× (z -10.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 50.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.255× (z -10.8) |
| [[A549 (line)]] | wt | 52.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 59.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7331), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CENPW]] | +0.64 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[POT1]] | +0.64 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[LSM2]] | +0.63 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[GUSBP18]] | +0.63 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[CDADC1]] | +0.62 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[MNAT1]] | +0.62 | +0.68 / +0.41 | both halves | 4e-05 |  |
| [[MED23]] | +0.62 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[ANAPC11]] | +0.61 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[THOC1]] | +0.61 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[GUSBP2-1]] | +0.61 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[ZNF45]] | +0.60 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[EEF1AKMT2]] | +0.60 | +0.56 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX5]] | -0.60 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[LINC00393]] | -0.56 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[CCDC200]] | -0.56 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[MC1R]] | -0.56 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[LINC01135]] | -0.55 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[KDM6B]] | -0.54 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[LINC00880]] | -0.54 | -0.50 / -0.27 | both halves | 3e-04 |  |
| [[FAM120AOS]] | -0.54 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[WDR45]] | -0.54 | -0.36 / -0.50 | both halves | 9e-05 |  |
| [[ARRDC3-AS1]] | -0.53 | -0.37 / -0.38 | both halves | 7e-05 |  |
| [[GRK4]] | -0.53 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[PXDC1]] | -0.52 | -0.41 / -0.46 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL27A1]] | B | COL27A1 activity lowers IMMP1L's level | lines that do not express COL27A1 (12) vs lines expressing it (38) | 1.35× higher at baseline in the lines without COL27A1 | 0.062 | ⚠ within organs, on part of the lines; also absent: C13orf46, ENSG00000285804, GSDME; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers IMMP1L's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[UGDH]] | C | UGDH activity lowers IMMP1L's level | lines that do not express UGDH (3) vs lines expressing it (47) | 1.40× higher at baseline in the lines without UGDH | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: B4GALT1, PYGB, TIMP1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.614). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-2.4, -11.7); signed map (-29.2, -10.8). **Vector** length 109, 28.7% of its response variance represented; |z| ≥ 3 in 1,139 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +5.5 | +5.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.9 | +9.6 |
|  | [[NG25 (drug)]] 5 µM |  | +4.3 | +3.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.0 | +7.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.9 | +9.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.2 | +2.6 |
|  | [[EX229 (drug)]] 5 µM |  | +2.1 | +1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +2.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.0 | +1.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.0 | +1.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.9 | -16.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.3 | -15.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.8 | -9.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.7 | -8.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.9 | -4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -2.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.3 | -5.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | inner mitochondrial membrane peptidase subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p13 — chr11:31,432,401-31,509,645 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25059; previously IMMP1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96LU5](https://www.uniprot.org/uniprotkb/Q96LU5) (Mitochondrial inner membrane protease subunit 1):

> Catalyzes the removal of transit peptides required for the targeting of proteins from the mitochondrial matrix, across the inner membrane, into the inter-membrane space. Known to process the nuclear encoded protein DIABLO.

**Summary**, from NCBI Gene [196294](https://www.ncbi.nlm.nih.gov/gene/196294):

> The mitochondrial inner membrane peptidase (IMP) complex generates mature, active proteins in the mitochondrial intermembrane space by proteolytically removing the mitochondrial targeting presequence of nuclear-encoded proteins. IMP1 and IMP2 (IMMP2L; MIM 605977) are the catalytic subunits of the IMP complex (Burri et al., 2005 [PubMed 15814844]).[supplied by OMIM, Sep 2008]

**Accessions** — [HGNC:26317](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26317) · Entrez [196294](https://www.ncbi.nlm.nih.gov/gene/196294) · UniProt [Q96LU5](https://www.uniprot.org/uniprotkb/Q96LU5) · Ensembl [ENSG00000148950](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148950)

## Data

Gene col 7331: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7331); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7331, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7331]; `tensor/DDL_lfc|DDL_z.npy` [7331]; `embed/gene_vectors.npy` [7331]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7331 or target_col == 7331). Every well: [[IMMP1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IMMP1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
