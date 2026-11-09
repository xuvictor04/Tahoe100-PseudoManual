---
symbol: "CASP8"
type: "gene"
col: 735
ensembl_id: "ENSG00000064012"
name: "caspase 8"
location: "2q33.1"
module: 32
arm: "+"
pooled_cpm: 59.04
n_lines_expressing: 47
n_dd_up: 16
n_dd_down: 3
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 16
direction_downstream: 6
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# CASP8

*caspase 8* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.35× (z +10.6, q 2e-23, up in 36 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.719× (z -7.9, q 1e-12, down in 28 of 44 measured lines) ⚠ toxic. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 5 µM: 0.828× (z -6.7, q 5e-09, down in 17 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 3 lines (NCI-H23 0.0972×, PANC-1 0.425×, COLO 205 0.404×; ⚠ toxic); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (BT-474 0.131×, CFPAC-1 0.382×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (RKO 0.357×, PANC-1 0.668×); [[Tofacitinib (drug)]] 5 µM in 1 line (LoVo 0.477×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (CFPAC-1 0.530×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRANK1]] (+0.65, fdr 1e-05), [[GBP3]] (+0.65, fdr 1e-05), [[IFIT2]] (+0.64, fdr 1e-05); moves opposite to [[PCMT1]] (-0.49, fdr 1e-04).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[RSAD2]] → it (grade B ⚠); 6 go from it, the strongest it → [[NMI]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 735.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +10.6 | 2e-23 | 36/45 (A-172, HOP62, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.35×** | +10.4 | 8e-23 | 28/45 (NCI-H2347, A-427, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +9.5 | 3e-19 | 30/45 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.40×** | +8.4 | 8e-15 | 29/45 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.26×** | +8.0 | 2e-13 | 23/45 (AsPC-1, NCI-H1573, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.33×** | +7.1 | 2e-10 | 29/45 (J82, SW1417, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.33×** | +6.8 | 7e-10 | 24/43 (A-172, BT-474, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.21×** | +6.6 | 2e-09 | 24/45 (J82, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +6.5 | 5e-09 | 27/45 (NCI-H460, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.25×** | +5.6 | 1e-06 | 24/46 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.22×** | +4.9 | 4e-05 | 22/45 (J82, A-172, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.21×** | +4.8 | 8e-05 | 21/45 (HS-578T, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.21×** | +4.6 | 2e-04 | 22/45 (AsPC-1, A549, …) | all doses, flat |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +4.6 | 2e-04 | 12/45 (NCI-H2030, SHP-77, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.40×** | +4.4 | 5e-04 | 21/46 (J82, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | 1.17× | +3.9 | 0.003 | 11/46 (CFPAC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.12× | +3.8 | 0.004 | 10/46 (CFPAC-1, LoVo, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.17× | +3.8 | 0.004 | 13/44 (LoVo, AsPC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.17× | +3.8 | 0.004 | 12/45 (A-172, HS-578T, …) | all doses, stronger at high dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.33×** | +3.7 | 0.005 | 13/43 (A-427, A498, …) | top dose only | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.16× | +3.6 | 0.009 | 9/45 (KATO III, LS 180, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.11× | +3.5 | 0.010 | 5/45 (LoVo, AsPC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.16× | +3.5 | 0.010 | 11/45 (LS 180, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 735.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 3 lines (NCI-H23 0.0972×, PANC-1 0.425×, COLO 205 0.404×; ⚠ toxic); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (BT-474 0.131×, CFPAC-1 0.382×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (RKO 0.357×, PANC-1 0.668×); [[Tofacitinib (drug)]] 5 µM in 1 line (LoVo 0.477×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (CFPAC-1 0.530×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.719×** | -7.9 | 1e-12 | 28/44 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.828×** | -6.7 | 5e-09 | 17/46 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.844× | -6.0 | 3e-07 | 19/46 (LoVo, COLO 205, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.862× | -5.3 | 2e-05 | 18/46 (LoVo, COLO 205, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.816×** | -5.1 | 4e-05 | 18/45 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.944× | -4.7 | 3e-04 | 1/46 (SNU-1) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | 0.866× | -3.6 | 0.025 | 11/46 (LoVo, SHP-77, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.868× | -3.4 | 0.043 | 10/45 (CFPAC-1, NCI-H23, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.875× | -3.4 | 0.051 | 15/45 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 0.879× | -3.2 | 0.066 | 12/45 (LoVo, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.884× | -3.1 | 0.093 | 13/45 (NCI-H460, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 735. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 51.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +19.8) | — |
| [[J82 (line)]] | alt | 61.7 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.72× (z +26.3) | — |
| [[HS-578T (line)]] | alt | 31.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +14.6) | — |
| [[A-427 (line)]] | wt | 44.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.69× (z +9.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 116 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +10.6) | — |
| [[NCI-H2347 (line)]] | alt | 36.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +10.1) | — |
| [[CFPAC-1 (line)]] | alt | 117 | 0 | 2 (1 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.530× (z -9.4) |
| [[COLO 205 (line)]] | alt | 149 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.345× (z -10.4) ⚠ cell-cycle shift, explains ~48% of this change |
| [[LoVo (line)]] | wt | 81.9 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +8.5) ⚠ cell-cycle shift, explains ~25% of this change | [[Tofacitinib (drug)]] 5 µM 0.477× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 81.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +10.4) | — |
| [[NCI-H460 (line)]] | wt | 92.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +21.6) | — |
| [[SK-MEL-2 (line)]] | alt | 58.6 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.82× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.86× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 63.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +15.9) | — |
| [[SW480 (line)]] | alt | 30.9 | 2 (2 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.69× (z +8.9) ⚠ cell-cycle shift, explains ~22% of this change | — |
| [[AsPC-1 (line)]] | alt | 50.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +13.4) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[BT-474 (line)]] | alt | 48.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.131× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 32.8 | 1 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.95× (z +9.3) | — |
| [[NCI-H1573 (line)]] | alt | 62.8 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +13.1) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[NCI-H23 (line)]] | alt | 24.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0972× (z -14.6) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 77.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.425× (z -12.3) ⚠ toxic |
| [[RKO (line)]] | wt | 58.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -12.1) |
| [[SW 900 (line)]] | alt | 49.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +10.9) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[A498 (line)]] | wt | 67.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 45.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.69 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 52.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 61.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 87.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 48.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 61.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.7 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 43.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 735), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRANK1]] | +0.65 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[GBP3]] | +0.65 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[IFIT2]] | +0.64 | +0.59 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[TRIM21]] | +0.64 | +0.60 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[IFI16]] | +0.63 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[IFI35]] | +0.63 | +0.54 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[IFIT3]] | +0.62 | +0.55 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[ZC3HAV1]] | +0.61 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[TLR3]] | +0.61 | +0.48 / +0.60 | both halves | 2e-05 | pathway: TLR3-mediated TICAM1-dependent programmed cell death; STRING 923 |
| [[PSMB8]] | +0.60 | +0.50 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[TRIM56]] | +0.60 | +0.67 / +0.45 | both halves | 3e-05 |  |
| [[IFIT5]] | +0.60 | +0.59 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCMT1]] | -0.49 | -0.53 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 12, C 4. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RSAD2]] | B | RSAD2 activity raises CASP8's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 1.97× lower at baseline in the lines without RSAD2 | 0.003 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[SP110]] | B | SP110 activity raises CASP8's level | lines that do not express SP110 (5) vs lines expressing it (45) | 2.02× lower at baseline in the lines without SP110 | 0.014 | ⚠ within organs, on part of the lines; also absent: IFIT1; maybe low, not absent |
| [[TRIM38]] | B | TRIM38 activity raises CASP8's level | lines that do not express TRIM38 (6) vs lines expressing it (44) | 2.59× lower at baseline in the lines without TRIM38 | 0.014 | ⚠ within organs, on part of the lines; also absent: SMOX, S100A13, ERAP2 |
| [[SP140L]] | B | SP140L activity raises CASP8's level | lines that do not express SP140L (5) vs lines expressing it (45) | 2.70× lower at baseline in the lines without SP140L | 0.016 | ⚠ within organs, on part of the lines; also absent: RNASEL, SP100, ALCAM; maybe low, not absent |
| [[SAMD9]] | B | SAMD9 activity raises CASP8's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 1.84× lower at baseline in the lines without SAMD9 | 0.018 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[OAS3]] | B | OAS3 activity raises CASP8's level | lines that do not express OAS3 (5) vs lines expressing it (45) | 2.19× lower at baseline in the lines without OAS3 | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000280007, PARP9, USP18 |
| [[APOL6]] | B | APOL6 activity raises CASP8's level | lines that do not express APOL6 (6) vs lines expressing it (44) | 2.39× lower at baseline in the lines without APOL6 | 0.031 | ⚠ within organs, on part of the lines; also absent: KLF4, S100A13, LGALS3BP; maybe low, not absent |
| [[DDX60]] | B | DDX60 activity raises CASP8's level | lines that do not express DDX60 (6) vs lines expressing it (44) | 1.88× lower at baseline in the lines without DDX60 | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000287188, RNASEL, SAMD9; maybe low, not absent |
| [[APOL3]] | B | APOL3 activity raises CASP8's level | lines that do not express APOL3 (14) vs lines expressing it (36) | 1.77× lower at baseline in the lines without APOL3 | 0.040 | ⚠ within organs, on part of the lines; also absent: SAMD9L, APOL1, GBP4 |
| [[BATF2]] | B | BATF2 activity raises CASP8's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 1.58× lower at baseline in the lines without BATF2 | 0.058 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |
| [[UBE2L6]] | B | UBE2L6 activity raises CASP8's level | lines that do not express UBE2L6 (6) vs lines expressing it (44) | 1.51× lower at baseline in the lines without UBE2L6 | 0.089 | ⚠ within organs, on part of the lines; also absent: BLVRA, ADAMTSL4, HLA-B |
| [[GBP4]] | B | GBP4 activity raises CASP8's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 1.39× lower at baseline in the lines without GBP4 | 0.096 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NMI]] | C | CASP8 activity raises NMI's level | lines that do not express CASP8 (3) vs lines expressing it (47) | 3.07× lower at baseline in the lines without CASP8 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with WNK2; also absent: PERP, SP100, PRRG1; maybe low, not absent; its own permutation p |
| [[SP110]] | C | CASP8 activity raises SP110's level | lines that do not express CASP8 (3) vs lines expressing it (47) | 1.93× lower at baseline in the lines without CASP8 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with WNK2; also absent: PERP, SP100, PRRG1; maybe low, not absent |
| [[TRIM21]] | C | CASP8 activity raises TRIM21's level | lines that do not express CASP8 (3) vs lines expressing it (47) | 1.82× lower at baseline in the lines without CASP8 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with WNK2; also absent: PERP, SP100, PRRG1; maybe low, not absent; its own permutation p |
| [[OAS3]] | C | CASP8 activity raises OAS3's level | lines that do not express CASP8 (3) vs lines expressing it (47) | 2.54× lower at baseline in the lines without CASP8 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with WNK2; also absent: PERP, SP100, PRRG1; maybe low, not absent; its own permutation p |
| [[PARP14]] | C | CASP8 activity raises PARP14's level | lines that do not express CASP8 (3) vs lines expressing it (47) | 2.51× lower at baseline in the lines without CASP8 | 0.098 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with WNK2; also absent: PERP, SP100, PRRG1; maybe low, not absent |
| [[PARP9]] | C | CASP8 activity raises PARP9's level | lines that do not express CASP8 (3) vs lines expressing it (47) | 2.47× lower at baseline in the lines without CASP8 | 0.099 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with WNK2; also absent: PERP, SP100, PRRG1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.610). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.6, 53.9); signed map (61.8, 32.1). **Vector** length 103, 24.5% of its response variance represented; |z| ≥ 3 in 1,041 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon* (control, mean cos +0.53 to 23); *Interferon Signaling* (reactome, mean cos +0.51 to 45); *Interferon alpha/beta signaling* (reactome, mean cos +0.51 to 27).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +6.4 | +10.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.2 | +10.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.8 | +4.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +5.8 | +8.4 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | +5.0 | +5.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +2.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.9 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +3.8 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -4.5 | -6.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.5 | -7.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | -4.3 | +4.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.1 | -2.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -3.9 | +4.6 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.8 | -5.3 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.5 | -3.6 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -3.5 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | caspase 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:201,233,443-201,361,836 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MCH5, MACH, FLICE, Casp-8 |
| Gene groups (HGNC) | Caspases; Death effector domain containing; Ripoptosome; Death inducing signaling complex |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, APOPTOSIS, INTERFERON_GAMMA_RESPONSE |
| Reactome | 56 pathways, smallest: Activation, myristolyation of BID and translocation to mitochondria; Microbial modulation of RIPK1-mediated regulated necrosis; FasL/ CD95L signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14790](https://www.uniprot.org/uniprotkb/Q14790) (Caspase-8):

> Thiol protease that plays a key role in programmed cell death by acting as a molecular switch for apoptosis, necroptosis and pyroptosis, and is required to prevent tissue damage during embryonic development and adulthood. Initiator protease that induces extrinsic apoptosis by mediating cleavage and activation of effector caspases downstream of FAS/CD95-mediated and TNFRSF1A-induced cell death. Cleaves and activates effector caspases CASP3, CASP4, CASP6, CASP7, CASP9 and CASP10. Binding to the …

**Summary**, from NCBI Gene [841](https://www.ncbi.nlm.nih.gov/gene/841):

> This gene encodes a member of the cysteine-aspartic acid protease (caspase) family. Sequential activation of caspases plays a central role in the execution-phase of cell apoptosis. Caspases exist as inactive proenzymes composed of a prodomain, a large protease subunit, and a small protease subunit. Activation of caspases requires proteolytic processing at conserved internal aspartic residues to generate a heterodimeric enzyme consisting of the large and small subunits. This protein is involved …

**Accessions** — [HGNC:1509](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1509) · Entrez [841](https://www.ncbi.nlm.nih.gov/gene/841) · UniProt [Q14790](https://www.uniprot.org/uniprotkb/Q14790) · Ensembl [ENSG00000064012](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000064012)

## Data

Gene col 735: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 735); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 735, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 735]; `tensor/DDL_lfc|DDL_z.npy` [735]; `embed/gene_vectors.npy` [735]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 735 or target_col == 735). Every well: [[CASP8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CASP8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
