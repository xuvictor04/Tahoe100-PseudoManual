---
symbol: "BCL2L2-PABPN1"
type: "gene"
col: 15121
ensembl_id: "ENSG00000258643"
name: "BCL2L2-PABPN1 readthrough"
location: "14q11.2"
module: 15
arm: "+"
pooled_cpm: 28.73
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 16
n_dd_up_clean: 11
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# BCL2L2-PABPN1

*BCL2L2-PABPN1 readthrough* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.46× (z +22.1, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.476× (z -12.9, q 3e-35, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF460-AS1]] (+0.74, fdr 1e-05), [[GARS1-DT]] (+0.72, fdr 1e-05), [[SAP30L-AS1]] (+0.70, fdr 1e-05); moves opposite to [[WDR7]] (-0.63, fdr 3e-05), [[COG2]] (-0.61, fdr 3e-05), [[TBC1D19]] (-0.57, fdr 5e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15121.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.46×** | +22.1 | 0e+00 | 43/48 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.30×** | +14.5 | 6e-45 | 46/48 (LoVo, A-427, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +11.0 | 7e-26 | 38/45 (NCI-H2030, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +11.0 | 9e-26 | 35/47 (NCI-H460, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +8.6 | 1e-15 | 35/48 (C32, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.60×** | +8.2 | 2e-14 | 31/48 (SW480, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +7.6 | 2e-12 | 32/46 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.47×** | +6.6 | 2e-09 | 30/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +6.2 | 4e-08 | 26/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.38×** | +5.6 | 1e-06 | 24/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +4.2 | 0.001 | 20/48 (hTERT-HPNE, A-172, …) | top dose only | position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | 1.15× | +3.5 | 0.018 | 12/48 (C-33 A, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.22×** | +3.5 | 0.022 | 13/47 (A-172, H4, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +3.4 | 0.032 | 17/48 (NCI-H2030, SW1417, …) | top dose only |  |
| [[TAK-733 (drug)]] 0.05 µM |  | **1.22×** | +3.3 | 0.036 | 8/48 (LOX-IMVI, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.058 | 14/47 (LOX-IMVI, MIA PaCa-2, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.082 | 9/47 (hTERT-HPNE, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15121.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.476×** | -12.9 | 3e-35 | 42/48 (C-33 A, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.513×** | -11.6 | 1e-28 | 41/48 (C-33 A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.554×** | -10.3 | 2e-22 | 37/48 (C-33 A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.626×** | -7.8 | 7e-13 | 34/47 (NCI-H1792, SNU-1, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.731×** | -7.7 | 1e-12 | 35/48 (LOX-IMVI, NCI-H460, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.633×** | -7.6 | 2e-12 | 33/48 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **0.735×** | -5.4 | 7e-06 | 23/45 (hTERT-HPNE, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.758×** | -4.8 | 1e-04 | 24/48 (SK-MEL-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.592×** | -4.8 | 1e-04 | 22/46 (NCI-H1573, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.784×** | -4.2 | 0.001 | 19/48 (C-33 A, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **0.782×** | -4.1 | 0.002 | 17/34 (NCI-H460, C-33 A, …) | top dose only | composition shift |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | **0.792×** | -3.8 | 0.006 | 13/48 (Hs 766T, A549, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.804×** | -3.8 | 0.006 | 16/48 (J82, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.945× | -3.7 | 0.008 | 1/48 (SW 1271) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.667×** | -3.7 | 0.009 | 9/48 (HCT15, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.699×** | -3.3 | 0.040 | 15/47 (SK-MEL-2, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.827×** | -3.2 | 0.050 | 9/47 (COLO 205, LoVo, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.836× | -3.1 | 0.059 | 17/48 (NCI-H1573, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 0.843× | -3.0 | 0.090 | 8/48 (NCI-H2030, KATO III, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15121. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 110 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.211× (z -11.9) |
| [[NCI-H460 (line)]] | wt | 36.6 | 2 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.187× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.332× (z -10.7) |
| [[HOP62 (line)]] | alt | 30.8 | 2 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.274× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.330× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 41.5 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.292× (z -10.4) |
| [[SK-MEL-2 (line)]] | alt | 52.2 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.253× (z -11.2) |
| [[A-427 (line)]] | wt | 19.0 | 2 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.38× (z +9.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.277× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 35.8 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 31.3 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.220× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 0.250× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 49.1 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.209× (z -12.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 0.330× (z -8.5) |
| [[SHP-77 (line)]] | alt | 22.7 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.48× (z +11.5) | [[Saquinavir (drug)]] 0.05 µM 0.121× (z -13.7) |
| [[SW480 (line)]] | alt | 25.9 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +9.2) | — |
| [[A549 (line)]] | wt | 23.5 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.266× (z -9.3) |
| [[C32 (line)]] | wt | 55.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -11.1) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 40.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.27× (z +9.9) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 43.8 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +9.5) | [[Belinostat (drug)]] 5 µM 0.221× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 20.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.74× (z +18.0) | — |
| [[A-172 (line)]] | wt | 25.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.61× (z +12.0) | — |
| [[A498 (line)]] | wt | 24.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +12.5) | — |
| [[AN3 CA (line)]] | alt | 22.8 | 0 | 1 | — | [[Delamanid (drug)]] 0.5 µM 0.0968× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 18.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +8.9) | — |
| [[BT-474 (line)]] | alt | 20.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +9.3) | — |
| [[Hs 766T (line)]] | wt | 37.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.235× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[HS-578T (line)]] | alt | 16.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +11.6) | — |
| [[J82 (line)]] | alt | 26.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.320× (z -8.8) |
| [[LoVo (line)]] | wt | 40.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.97× (z +10.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 52.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.176× (z -15.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 18.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +10.1) | — |
| [[Panc 03.27 (line)]] | alt | 17.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +11.4) | — |
| [[PANC-1 (line)]] | alt | 12.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +13.1) | — |
| [[RKO (line)]] | wt | 22.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 51.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.17× (z +8.6) | — |
| [[SNU-1 (line)]] | wt | 39.1 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.153× (z -10.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW 900 (line)]] | alt | 19.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +10.2) | — |
| [[SW1417 (line)]] | alt | 16.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.22× (z +10.5) | — |
| [[SW48 (line)]] | wt | 22.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[CHP-212 (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15121), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 4 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF460-AS1]] | +0.74 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[GARS1-DT]] | +0.72 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[SAP30L-AS1]] | +0.70 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[VPS13B-DT]] | +0.70 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[NMNAT1]] | +0.67 | +0.36 / +0.63 | both halves | 9e-05 |  |
| [[NRSN2-AS1]] | +0.67 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[SLC25A53]] | +0.66 | +0.40 / +0.60 | both halves | 4e-05 |  |
| [[ZNF213-AS1]] | +0.66 | +0.35 / +0.63 | both halves | 1e-04 |  |
| [[NADSYN1]] | +0.66 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[C9orf153]] | +0.65 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[PELO-AS1]] | +0.65 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[BCL2L2]] | +0.65 | +0.58 / +0.58 | both halves | 8e-06 | STRING 554; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[CDK2AP1]] | +0.65 | +0.47 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR7]] | -0.63 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[COG2]] | -0.61 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[TBC1D19]] | -0.57 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[PABIR1]] | -0.55 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[WDR70]] | -0.55 | -0.36 / -0.41 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers BCL2L2-PABPN1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.754). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-3.6, 22.6); signed map (2.5, 1.4). **Vector** length 121, 32.5% of its response variance represented; |z| ≥ 3 in 1,167 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.7 | +14.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.6 | +22.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +9.5 | +11.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.7 | +8.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.8 | +11.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.8 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | +4.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +3.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.5 | +2.9 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -7.1 | -12.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.7 | -11.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -5.6 | -7.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.3 | -10.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | -7.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.7 | -7.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.3 | -3.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.0 | -3.1 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.5 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | BCL2L2-PABPN1 readthrough |
| Locus type | readthrough (other) |
| Location | 14q11.2 — chr14:23,306,833-23,326,175 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92843](https://www.uniprot.org/uniprotkb/Q92843) (Bcl-2-like protein 2):

> Promotes cell survival. Blocks dexamethasone-induced apoptosis. Mediates survival of postmitotic Sertoli cells by suppressing death-promoting activity of BAX.

**Summary**, from NCBI Gene [100529063](https://www.ncbi.nlm.nih.gov/gene/100529063):

> This locus represents naturally occurring read-through transcription between the neighboring BCL2L2 (BCL2-like 2) and PABPN1 (poly(A) binding protein, nuclear 1) genes on chromosome 14. The read-through transcript encodes a fusion protein that shares sequence identity with each individual gene product. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:42959](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:42959) · Entrez [100529063](https://www.ncbi.nlm.nih.gov/gene/100529063) · UniProt [Q92843](https://www.uniprot.org/uniprotkb/Q92843) · Ensembl [ENSG00000258643](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000258643)

## Data

Gene col 15121: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15121); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15121, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15121]; `tensor/DDL_lfc|DDL_z.npy` [15121]; `embed/gene_vectors.npy` [15121]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15121 or target_col == 15121). Every well: [[BCL2L2-PABPN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCL2L2-PABPN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
