---
symbol: "GSTCD"
type: "gene"
col: 6238
ensembl_id: "ENSG00000138780"
name: "glutathione S-transferase C-terminal domain containing"
location: "4q24"
module: 6
arm: "+"
pooled_cpm: 41.95
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 4
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# GSTCD

*glutathione S-transferase C-terminal domain containing* — 4q24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.73× (z +29.4, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.579× (z -5.9, q 2e-06, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RMI1]] (+0.71, fdr 7e-06), [[DDIAS]] (+0.71, fdr 7e-06), [[VRK1]] (+0.69, fdr 7e-06); moves opposite to [[TBC1D17]] (-0.60, fdr 1e-05), [[UBE2B]] (-0.57, fdr 2e-05), [[SHC2]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6238.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.73×** | +29.4 | 0e+00 | 48/48 (CFPAC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **3.33×** | +23.9 | 0e+00 | 44/47 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.16×** | +22.8 | 0e+00 | 44/48 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.99×** | +14.3 | 6e-44 | 46/48 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.61×** | +13.9 | 5e-42 | 37/48 (SW1417, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.83×** | +12.5 | 7e-34 | 46/48 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.82×** | +12.4 | 3e-33 | 43/48 (A498, NCI-H1573, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~68% of this change | **1.48×** | +7.8 | 4e-13 | 31/47 (RKO, HT-29, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.41×** | +7.1 | 6e-11 | 31/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.81×** | +6.4 | 9e-09 | 32/48 (SK-MEL-2, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.35×** | +6.2 | 3e-08 | 28/48 (SK-MEL-2, COLO 205, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.34×** | +5.8 | 2e-07 | 26/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **1.32×** | +5.7 | 4e-07 | 22/47 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.30×** | +5.5 | 2e-06 | 23/47 (A498, RPMI-7951, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.61×** | +5.2 | 9e-06 | 16/34 (SW480, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +4.5 | 2e-04 | 20/48 (NCI-H2347, A498, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.17× | +3.0 | 0.068 | 10/47 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 1.16× | +2.9 | 0.093 | 4/48 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 1.15× | +2.9 | 0.099 | 7/48 (A498, HCT15, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6238.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.579×** | -5.9 | 2e-06 | 27/48 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.814×** | -4.1 | 0.013 | 21/47 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.699×** | -3.9 | 0.022 | 19/48 (RKO, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.774×** | -3.8 | 0.024 | 18/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.890× | -3.4 | 0.084 | 10/48 (PANC-1, KATO III, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | 0.855× | -3.2 | 0.11 | 6/48 (A498, HT-29, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.804× | -3.2 | 0.11 | 10/47 (CFPAC-1, SW 1271, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~59% of this change | 0.854× | -3.1 | 0.15 | 9/48 (LoVo, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.77 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6238. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 38.5 | 6 (3 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.19× (z +14.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 4.99× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.282× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 40.3 | 5 (3 ⚠) | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 5.70× (z +12.7) | — |
| [[CFPAC-1 (line)]] | alt | 32.5 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.84× (z +19.6) | — |
| [[HEC-1-A (line)]] | alt | 93.1 | 4 (1 ⚠) | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.70× (z +15.4) | — |
| [[HOP62 (line)]] | alt | 41.0 | 4 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 6.14× (z +15.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 4.81× (z +13.4) | — |
| [[NCI-H460 (line)]] | wt | 48.3 | 3 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.49× (z +15.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.140× (z -24.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 37.0 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +17.3) | — |
| [[A498 (line)]] | wt | 46.0 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.11× (z +11.4) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[BT-474 (line)]] | alt | 46.1 | 3 (1 ⚠) | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.91× (z +11.2) | — |
| [[COLO 205 (line)]] | alt | 36.1 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +10.4) | — |
| [[H4 (line)]] | wt | 39.6 | 2 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 7.49× (z +11.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 5.63× (z +9.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.220× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 21.4 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.19× (z +16.0) | — |
| [[HT-29 (line)]] | alt | 37.7 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +13.4) | — |
| [[hTERT-HPNE (line)]] | wt | 26.7 | 3 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 9.53× (z +12.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 6.83× (z +10.4) | — |
| [[LOX-IMVI (line)]] | wt | 41.9 | 3 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.37× (z +12.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +11.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 37.6 | 3 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 9.16× (z +18.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 8.76× (z +18.5) | — |
| [[NCI-H1573 (line)]] | alt | 54.3 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +10.9) | — |
| [[NCI-H2030 (line)]] | alt | 23.8 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.65× (z +17.1) | — |
| [[NCI-H2347 (line)]] | alt | 33.9 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.27× (z +15.8) | — |
| [[Panc 03.27 (line)]] | alt | 39.2 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +14.6) | — |
| [[RPMI-7951 (line)]] | alt | 32.2 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.37× (z +13.5) | — |
| [[SK-MEL-2 (line)]] | alt | 55.0 | 2 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.82× (z +14.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.32× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.220× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 15.2 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.03× (z +13.9) | — |
| [[SW 900 (line)]] | alt | 30.9 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.86× (z +13.2) | — |
| [[SW1417 (line)]] | alt | 38.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +17.8) | — |
| [[SW480 (line)]] | alt | 37.6 | 3 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.02× (z +16.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +15.0) | — |
| [[C-33 A (line)]] | alt | 69.5 | 2 | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.81× (z +10.7) | — |
| [[C32 (line)]] | wt | 46.7 | 2 (1 ⚠) | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 5.34× (z +13.2) | — |
| [[HCT15 (line)]] | alt | 52.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +9.9) | [[Digitoxin (drug)]] 5 µM 0.239× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 37.2 | 2 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +10.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +9.0) | — |
| [[A-427 (line)]] | wt | 62.2 | 1 | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +8.9) | — |
| [[A549 (line)]] | wt | 43.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.255× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 22.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.03× (z +18.3) | — |
| [[CHP-212 (line)]] | wt | 50.1 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0575× (z -11.4) |
| [[Hs 766T (line)]] | wt | 30.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.41× (z +12.6) | — |
| [[KATO III (line)]] | alt | 46.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +9.1) | — |
| [[LoVo (line)]] | wt | 56.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +16.1) | — |
| [[NCI-H1792 (line)]] | alt | 38.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +11.8) | — |
| [[SHP-77 (line)]] | alt | 30.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +12.3) | — |
| [[SW48 (line)]] | wt | 33.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +10.3) | — |
| [[AN3 CA (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 58.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6238), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RMI1]] | +0.71 | +0.69 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[DDIAS]] | +0.71 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[VRK1]] | +0.69 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[KNTC1]] | +0.68 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[PRIMPOL]] | +0.66 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[NUP205]] | +0.64 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[DYRK4]] | +0.64 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[TYMS]] | +0.64 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[FANCM]] | +0.64 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[CSE1L]] | +0.63 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[RAD51AP1]] | +0.61 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[SUV39H2]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D17]] | -0.60 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[UBE2B]] | -0.57 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[SHC2]] | -0.56 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[SYP]] | -0.56 | -0.49 / -0.40 | both halves | 4e-05 |  |
| [[TBC1D25]] | -0.55 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[SUPT5H]] | -0.54 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[GNG7]] | -0.53 | -0.37 / -0.41 | both halves | 7e-05 |  |
| [[HDAC5]] | -0.53 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[SHF]] | -0.52 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[BEX4]] | -0.52 | -0.36 / -0.53 | both halves | 9e-05 |  |
| [[WBP2]] | -0.52 | -0.37 / -0.56 | both halves | 9e-05 |  |
| [[ASMTL]] | -0.52 | -0.51 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GSTCD's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.570). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-38.3, -45.8); signed map (-40.5, -47.9). **Vector** length 101, 26.3% of its response variance represented; |z| ≥ 3 in 1,106 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *CDC6 association with the ORC:origin complex* (reactome, mean cos +0.51 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +8.3 | +23.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +22.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.0 | +7.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +13.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.4 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +4.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.5 | +2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +3.0 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +2.1 | +2.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.7 | -1.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.7 | +2.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.2 | -2.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.8 | +0.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.3 | +1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -0.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -3.1 | -2.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | -3.0 | -2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | glutathione S-transferase C-terminal domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q24 — chr4:105,708,778-105,847,725 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13273 |
| Gene groups (HGNC) | 7BS orphan methyltransferases |
| Matched by | ensembl_id |

UniProt [Q8NEC7](https://www.uniprot.org/uniprotkb/Q8NEC7) carries no function annotation.

**Summary**, from NCBI Gene [79807](https://www.ncbi.nlm.nih.gov/gene/79807):

> Predicted to act upstream of or within respiratory system development and response to lipopolysaccharide. Located in cytoplasm and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25806](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25806) · Entrez [79807](https://www.ncbi.nlm.nih.gov/gene/79807) · UniProt [Q8NEC7](https://www.uniprot.org/uniprotkb/Q8NEC7) · Ensembl [ENSG00000138780](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138780)

## Data

Gene col 6238: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6238); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6238, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6238]; `tensor/DDL_lfc|DDL_z.npy` [6238]; `embed/gene_vectors.npy` [6238]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6238 or target_col == 6238). Every well: [[GSTCD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GSTCD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
