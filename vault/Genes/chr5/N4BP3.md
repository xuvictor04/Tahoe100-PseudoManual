---
symbol: "N4BP3"
type: "gene"
col: 7040
ensembl_id: "ENSG00000145911"
name: "NEDD4 binding protein 3"
location: "5q35.3"
module: 206
arm: "+"
pooled_cpm: 12.2
n_lines_expressing: 44
n_dd_up: 16
n_dd_down: 37
n_dd_up_clean: 15
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/206"]
generated_by: "tahoemap"
---

# N4BP3

*NEDD4 binding protein 3* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.09× (z +26.2, q 0e+00, up in 36 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (7 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.513× (z -10.7, q 4e-24, down in 33 of 42 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.567× (z -9.1, q 2e-17, down in 27 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM29]] (+0.71, fdr 7e-06), [[CYTH4]] (+0.69, fdr 7e-06), [[PDGFB]] (+0.65, fdr 1e-05); moves opposite to [[ADPGK]] (-0.65, fdr 7e-06), [[SDHD]] (-0.62, fdr 1e-05), [[KPNA6]] (-0.60, fdr 1e-05).
> It is in [[Module 206]], a single-armed module (Constitutive Signaling by Aberrant PI3K in Cancer).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PDGFB]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7040.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.09×** | +26.2 | 0e+00 | 36/41 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.94×** | +11.8 | 1e-29 | 34/41 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.42×** | +10.1 | 1e-21 | 27/40 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +6.8 | 2e-09 | 24/42 (SW 900, SW1417, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.60×** | +5.4 | 8e-06 | 22/42 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.50×** | +4.3 | 0.001 | 18/41 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **2.07×** | +4.3 | 0.001 | 13/40 (CFPAC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.46×** | +4.3 | 0.001 | 18/42 (LoVo, KATO III, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.41×** | +3.9 | 0.006 | 16/42 (NCI-H2347, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.41×** | +3.9 | 0.006 | 17/42 (A-172, A549, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.39×** | +3.7 | 0.010 | 16/42 (NCI-H460, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.38×** | +3.6 | 0.013 | 14/42 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.83×** | +3.6 | 0.014 | 15/42 (PANC-1, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.34×** | +3.2 | 0.055 | 12/40 (RPMI-7951, SHP-77, …) | top dose only |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.70×** | +3.1 | 0.062 | 5/42 (SW480, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Hexylresorcinol (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.070 | 8/42 (HS-578T, PANC-1, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7040.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.513×** | -10.7 | 4e-24 | 33/42 (SK-MEL-2, SNU-423, …) | rises with dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.567×** | -9.1 | 2e-17 | 27/40 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.440×** | -9.0 | 5e-17 | 27/41 (A-172, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.472×** | -8.2 | 3e-14 | 28/41 (MIA PaCa-2, A-172, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.656×** | -6.8 | 1e-09 | 27/42 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.561×** | -6.2 | 7e-08 | 26/42 (AsPC-1, HEC-1-A, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.585×** | -5.9 | 4e-07 | 23/42 (A549, HEC-1-A, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.379×** | -5.8 | 6e-07 | 22/36 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.726×** | -5.0 | 4e-05 | 19/42 (HEC-1-A, MIA PaCa-2, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.636×** | -4.9 | 7e-05 | 16/41 (HEC-1-A, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.656×** | -4.8 | 9e-05 | 21/42 (HCT15, NCI-H1792, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.641×** | -4.8 | 9e-05 | 21/41 (PANC-1, SK-MEL-2, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.662×** | -4.7 | 1e-04 | 19/42 (C-33 A, HCT15, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.645×** | -4.7 | 1e-04 | 20/42 (HEC-1-A, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.655×** | -4.6 | 1e-04 | 21/42 (HEC-1-A, MIA PaCa-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.725×** | -4.5 | 2e-04 | 19/42 (HEC-1-A, CHP-212, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.720×** | -4.5 | 2e-04 | 16/42 (HEC-1-A, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7040. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 40.0 | 2 | 9 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.0640× (z -22.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -13.8) |
| [[A-172 (line)]] | wt | 9.20 | 3 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 16.4× (z +17.8) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0662× (z -11.7) |
| [[NCI-H1573 (line)]] | alt | 33.9 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.40× (z +19.1) | [[Dinaciclib (drug)]] 5 µM 0.183× (z -9.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 10.3 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 15.7× (z +16.1) | [[Selinexor (drug)]] 5 µM 0.109× (z -12.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.105× (z -8.9) |
| [[A549 (line)]] | wt | 19.2 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +13.7) | [[Selinexor (drug)]] 5 µM 0.236× (z -11.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.152× (z -10.3) |
| [[MIA PaCa-2 (line)]] | alt | 25.0 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 7.97× (z +20.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -16.3) |
| [[NCI-H2347 (line)]] | alt | 7.28 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 16.0× (z +18.4) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.102× (z -10.3) |
| [[PANC-1 (line)]] | alt | 11.2 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +23.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -12.7) |
| [[RPMI-7951 (line)]] | alt | 32.2 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +11.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -13.0) |
| [[NCI-H460 (line)]] | wt | 10.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.84× (z +15.4) | — |
| [[A-427 (line)]] | wt | 18.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +10.5) | — |
| [[AsPC-1 (line)]] | alt | 5.00 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 18.1× (z +14.4) | [[Cobimetinib (drug)]] 5 µM 0.0575× (z -9.6) |
| [[BT-474 (line)]] | alt | 13.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.79× (z +12.6) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.101× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 12.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.73× (z +11.8) | [[Selinexor (drug)]] 5 µM 0.211× (z -11.7) ⚠ cell-cycle shift, explains ~30% of this change |
| [[Hs 766T (line)]] | wt | 7.52 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.83× (z +11.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.138× (z -10.3) |
| [[HS-578T (line)]] | alt | 8.18 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.31× (z +12.4) | [[Selinexor (drug)]] 5 µM 0.222× (z -8.8) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H1792 (line)]] | alt | 24.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -13.0) |
| [[NCI-H23 (line)]] | alt | 8.56 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +9.8) | [[Panobinostat (drug)]] 0.5 µM 0.0990× (z -10.2) |
| [[SHP-77 (line)]] | alt | 8.51 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0586× (z -10.1) ⚠ cell-cycle shift, explains ~91% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.182× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 22.3 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.159× (z -13.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -10.6) |
| [[COLO 205 (line)]] | alt | 5.30 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 31.6× (z +13.0) | — |
| [[H4 (line)]] | wt | 12.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.02× (z +9.6) | — |
| [[HCT15 (line)]] | alt | 6.48 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.0655× (z -8.6) |
| [[HOP62 (line)]] | alt | 15.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +12.6) | — |
| [[KATO III (line)]] | alt | 8.50 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +8.9) | — |
| [[LoVo (line)]] | wt | 15.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +13.0) | — |
| [[NCI-H2030 (line)]] | alt | 10.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +13.2) | — |
| [[Panc 03.27 (line)]] | alt | 14.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.90× (z +10.9) | — |
| [[RKO (line)]] | wt | 17.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +10.1) | — |
| [[SW 1271 (line)]] | alt | 31.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0792× (z -9.9) |
| [[SW 900 (line)]] | alt | 9.45 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.8× (z +17.2) | — |
| [[SW1417 (line)]] | alt | 6.67 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.52× (z +10.6) | — |
| [[SW48 (line)]] | wt | 8.70 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.14× (z +9.8) | — |
| [[A498 (line)]] | wt | 1.86 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.23 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 10.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7040), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM29]] | +0.71 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[CYTH4]] | +0.69 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[PDGFB]] | +0.65 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[NFKBIE]] | +0.64 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[PIK3CD]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[DRAP1]] | +0.63 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[HMGA1]] | +0.63 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[RELA]] | +0.63 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[BTG1]] | +0.62 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[MIDEAS]] | +0.62 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[TNIP2]] | +0.62 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[RIN1]] | +0.62 | +0.62 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADPGK]] | -0.65 | -0.59 / -0.69 | both halves | 7e-06 |  |
| [[SDHD]] | -0.62 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[KPNA6]] | -0.60 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[GTF2I]] | -0.60 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[CMPK1]] | -0.57 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[MRPS15]] | -0.56 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[PSMB2]] | -0.56 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[ATP2A2]] | -0.55 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[NNT]] | -0.54 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[ZNF148]] | -0.54 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[GNAQ]] | -0.54 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[CSDE1]] | -0.53 | -0.41 / -0.49 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises N4BP3's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 6.7% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[BCAN-AS1]] | B | BCAN-AS1 activity raises N4BP3's level | lines that do not express BCAN-AS1 (11) vs lines expressing it (39) | 1.87× lower at baseline in the lines without BCAN-AS1 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000272405, BCAN-AS2, ETV7; maybe low, not absent |
| [[NNT]] | B | NNT activity lowers N4BP3's level | lines that do not express NNT (6) vs lines expressing it (44) | 1.60× higher at baseline in the lines without NNT | 0.051 | ⚠ within organs, on part of the lines; co-absent genes |
| [[TOP2A]] | B | TOP2A activity raises N4BP3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDGFB]] | B | N4BP3 activity raises PDGFB's level | lines that do not express N4BP3 (6) vs lines expressing it (44) | 2.31× lower at baseline in the lines without N4BP3 | 0.060 | ⚠ within organs, on part of the lines; also absent: KIAA1522, ENSG00000257489, CCDC88C; its own permutation p |

## Where it sits

- **Module**: [[Module 206]] — Constitutive Signaling by Aberrant PI3K in Cancer; 15 genes; every member is in the + arm (projection on the module's main direction 0.878). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (40.3, -2.0); signed map (-1.2, 43.1). **Vector** length 113, 28.8% of its response variance represented; |z| ≥ 3 in 1,165 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.3 | +26.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.6 | +6.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.4 | +5.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.1 | +11.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.5 | +10.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.1 | +4.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +1.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.1 | +1.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -5.3 | -10.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.0 | -6.8 |
|  | [[NG25 (drug)]] 5 µM |  | -4.6 | -5.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -4.6 | -4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.7 | -4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.4 | -2.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.2 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | NEDD4 binding protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:178,113,532-178,126,081 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LZTS4 |
| Gene groups (HGNC) | Leucine zipper tumor suppressor family |
| Matched by | ensembl_id |

**Function**, from UniProt [O15049](https://www.uniprot.org/uniprotkb/O15049) (NEDD4-binding protein 3):

> Plays a positive role in the antiviral innate immune signaling pathway. Mechanistically, interacts with MAVS and functions as a positive regulator to promote 'Lys-63'-linked polyubiquitination of MAVS and thus strengthens the interaction between MAVS and TRAF2. Also plays a role in axon and dendrite arborization during cranial nerve development. May also be important for neural crest migration and early development of other anterior structures including eye, brain and cranial cartilage (By …

**Summary**, from NCBI Gene [23138](https://www.ncbi.nlm.nih.gov/gene/23138):

> Predicted to be involved in innate immune response and nervous system development. Predicted to be located in axon and dendrite. Predicted to be active in cytoplasmic vesicle. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29852](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29852) · Entrez [23138](https://www.ncbi.nlm.nih.gov/gene/23138) · UniProt [O15049](https://www.uniprot.org/uniprotkb/O15049) · Ensembl [ENSG00000145911](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145911)

## Data

Gene col 7040: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7040); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7040, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7040]; `tensor/DDL_lfc|DDL_z.npy` [7040]; `embed/gene_vectors.npy` [7040]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7040 or target_col == 7040). Every well: [[N4BP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/N4BP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
