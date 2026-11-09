---
symbol: "TRIM5"
type: "gene"
col: 5289
ensembl_id: "ENSG00000132256"
name: "tripartite motif containing 5"
location: "11p15.4"
module: 70
arm: "+"
pooled_cpm: 64.86
n_lines_expressing: 49
n_dd_up: 16
n_dd_down: 31
n_dd_up_clean: 13
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 23
direction_downstream: 5
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# TRIM5

*tripartite motif containing 5* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 2.20× (z +13.4, q 4e-38, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.620× (z -8.4, q 2e-14, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMB9]] (+0.81, fdr 7e-06), [[IFI27]] (+0.80, fdr 7e-06), [[ISG15]] (+0.79, fdr 7e-06).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[TRIM34]] → it (grade B ⚠); 5 go from it, the strongest it → [[NMI]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5289.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **2.20×** | +13.4 | 4e-38 | 40/47 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.71×** | +13.3 | 7e-38 | 34/47 (PANC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.05×** | +12.6 | 4e-34 | 37/47 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.83×** | +10.6 | 4e-24 | 39/47 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.46×** | +6.7 | 2e-09 | 33/47 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +5.8 | 8e-07 | 30/47 (BT-474, PANC-1, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +5.5 | 3e-06 | 26/47 (NCI-H2347, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +5.4 | 4e-06 | 24/47 (SNU-1, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.34×** | +5.0 | 4e-05 | 27/46 (AsPC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.31×** | +4.8 | 1e-04 | 26/47 (CFPAC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +4.4 | 5e-04 | 23/47 (SW480, SW1417, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.20× | +4.4 | 6e-04 | 21/47 (CFPAC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.1 | 0.002 | 1/48 (MIA PaCa-2) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **1.55×** | +4.1 | 0.002 | 23/46 (LoVo, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.26×** | +3.9 | 0.004 | 20/47 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.24×** | +3.8 | 0.005 | 18/48 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.7 | 0.009 | 22/47 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5289.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.620×** | -8.4 | 2e-14 | 29/47 (HS-578T, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.717×** | -8.3 | 3e-14 | 28/47 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.633×** | -8.1 | 1e-13 | 34/47 (RPMI-7951, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.627×** | -7.9 | 4e-13 | 28/46 (SNU-423, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.647×** | -7.1 | 1e-10 | 27/43 (SK-MEL-2, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.672×** | -6.7 | 2e-09 | 24/39 (RPMI-7951, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.698×** | -6.3 | 2e-08 | 26/47 (HS-578T, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.719×** | -5.8 | 5e-07 | 25/47 (SNU-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.721×** | -5.8 | 5e-07 | 28/47 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.802×** | -5.5 | 2e-06 | 24/48 (AsPC-1, A549, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.743×** | -5.2 | 8e-06 | 22/47 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.756×** | -4.9 | 4e-05 | 24/47 (LoVo, RPMI-7951, …) | top dose only |  |
| [[crizotinib (drug)]] 5 µM |  | **0.765×** | -4.5 | 2e-04 | 23/47 (SNU-423, A549, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.835× | -4.5 | 3e-04 | 23/47 (BT-474, MIA PaCa-2, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.788×** | -4.2 | 0.001 | 21/47 (SNU-423, BT-474, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.790×** | -4.1 | 0.001 | 23/47 (MIA PaCa-2, SNU-423, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.802×** | -3.9 | 0.004 | 20/47 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.858× | -3.8 | 0.004 | 18/47 (LoVo, Hs 766T, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.809×** | -3.7 | 0.005 | 19/47 (LOX-IMVI, A549, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5289. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 109 | 3 | 9 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.58× (z +12.2) | [[Tofacitinib (drug)]] 5 µM 0.381× (z -13.0) |
| [[A-172 (line)]] | wt | 151 | 3 | 7 (4 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.94× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.274× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.425× (z -13.0) |
| [[BT-474 (line)]] | alt | 107 | 4 (3 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.59× (z +10.7) | [[TAK-901 (drug)]] 0.05 µM 0.269× (z -10.4) |
| [[NCI-H2347 (line)]] | alt | 58.3 | 4 | 2 | [[Harringtonine (drug)]] 5 µM 4.98× (z +15.1) | [[Tofacitinib (drug)]] 5 µM 0.396× (z -12.7) |
| [[AsPC-1 (line)]] | alt | 71.0 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +12.3) | [[Tofacitinib (drug)]] 5 µM 0.404× (z -11.0) |
| [[RPMI-7951 (line)]] | alt | 103 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.435× (z -10.5) |
| [[A549 (line)]] | wt | 106 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.209× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.378× (z -12.0) |
| [[Hs 766T (line)]] | wt | 123 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +16.2) | [[Dinaciclib (drug)]] 5 µM 0.317× (z -11.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 62.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +21.8) | — |
| [[SK-MEL-2 (line)]] | alt | 69.2 | 3 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +13.4) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.68× (z +13.3) | [[Dinaciclib (drug)]] 0.05 µM 0.0714× (z -23.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 103 | 0 | 4 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.186× (z -14.2) ⚠ toxic · without an alert: [[Tofacitinib (drug)]] 5 µM 0.408× (z -11.1) |
| [[A498 (line)]] | wt | 98.8 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.412× (z -10.1) ⚠ toxic · without an alert: [[Tofacitinib (drug)]] 5 µM 0.563× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 62.1 | 2 | 1 | [[Harringtonine (drug)]] 5 µM 3.01× (z +10.3) | [[Tofacitinib (drug)]] 5 µM 0.449× (z -11.0) |
| [[HS-578T (line)]] | alt | 143 | 1 | 2 | [[Homoharringtonine (drug)]] 0.5 µM 2.37× (z +8.7) | [[Belinostat (drug)]] 5 µM 0.342× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 47.3 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 2.83× (z +9.3) | — |
| [[A-427 (line)]] | wt | 40.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.60× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.254× (z -11.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 48.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +11.8) | — |
| [[HOP62 (line)]] | alt | 27.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +13.3) | — |
| [[J82 (line)]] | alt | 69.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +13.3) | — |
| [[LoVo (line)]] | wt | 81.2 | 1 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.56× (z +9.8) | [[Belinostat (drug)]] 5 µM 0.440× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 61.4 | 0 | 2 | — | [[Tofacitinib (drug)]] 5 µM 0.425× (z -10.0) |
| [[SNU-1 (line)]] | wt | 113 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.0787× (z -21.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 24.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.49× (z +11.7) | — |
| [[SW480 (line)]] | alt | 23.4 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.12× (z +9.4) | — |
| [[AN3 CA (line)]] | alt | 52.7 | 0 | 1 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.132× (z -9.8) |
| [[COLO 205 (line)]] | alt | 84.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.424× (z -9.3) ⚠ cell-cycle shift, explains ~39% of this change |
| [[KATO III (line)]] | alt | 41.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0750× (z -22.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 75.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.253× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 82.3 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.58× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 43.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +9.1) | — |
| [[NCI-H23 (line)]] | alt | 42.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +11.0) | — |
| [[Panc 03.27 (line)]] | alt | 36.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -9.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 53.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.94× (z +8.5) | — |
| [[C-33 A (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 91.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 46.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 55.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.1 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 73.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5289), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMB9]] | +0.81 | +0.75 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[IFI27]] | +0.80 | +0.73 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[ISG15]] | +0.79 | +0.78 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 577 |
| [[IFIH1]] | +0.79 | +0.74 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 565 |
| [[DDX60]] | +0.78 | +0.74 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 486 |
| [[PLEKHA4]] | +0.78 | +0.74 / +0.76 | both halves | 7e-06 |  |
| [[HLA-B]] | +0.77 | +0.74 / +0.74 | both halves | 7e-06 | pathway: Interferon Signaling |
| [[IFI44]] | +0.77 | +0.69 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 411 |
| [[DHX58]] | +0.77 | +0.66 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 426 |
| [[DDX60L]] | +0.77 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[HLA-F]] | +0.77 | +0.72 / +0.75 | both halves | 7e-06 | pathway: Interferon Signaling |
| [[PARP10]] | +0.77 | +0.72 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 17, C 6. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIM34]] | B | TRIM34 activity raises TRIM5's level | lines that do not express TRIM34 (6) vs lines expressing it (44) | 2.02× lower at baseline in the lines without TRIM34 | 0.011 | ⚠ within organs, on part of the lines; also absent: BIRC3, FXYD5, TFAP2A; maybe low, not absent |
| [[SAMD9L]] | B | SAMD9L activity strengthens TRIM5's drug response | lines that do not express SAMD9L (18) vs lines expressing it (29) | the lines without SAMD9L respond 0.73× as strongly (z diff +0.72); strongest at Niclosamide (olamine) 5 µM: 0.85x vs 0.58x (z diff +3.2) | 0.020 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22; target measured in part of the lines; artifact flags |
| [[IL15RA]] | B | IL15RA activity raises TRIM5's level | lines that do not express IL15RA (7) vs lines expressing it (43) | 2.19× lower at baseline in the lines without IL15RA | 0.039 | ⚠ within organs, on part of the lines; also absent: CLCF1, SGMS2 |
| [[CD5L]] | B | CD5L activity raises TRIM5's level | lines that do not express CD5L (23) vs lines expressing it (27) | 1.61× lower at baseline in the lines without CD5L | 0.044 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent |
| [[ERAP2]] | B | ERAP2 activity raises TRIM5's level | lines that do not express ERAP2 (7) vs lines expressing it (43) | 1.95× lower at baseline in the lines without ERAP2 | 0.048 | ⚠ within organs, on part of the lines; also absent: COL13A1, SMOX, TRIM38; maybe low, not absent |
| [[TRIM22]] | B | TRIM22 activity raises TRIM5's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 1.82× lower at baseline in the lines without TRIM22 | 0.055 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[MAP2K1]] | B | MAP2K1 activity lowers TRIM5's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[IFIT2]] | B | IFIT2 activity raises TRIM5's level | lines that do not express IFIT2 (8) vs lines expressing it (42) | 1.88× lower at baseline in the lines without IFIT2 | 0.061 | ⚠ within organs, on part of the lines; also absent: IFIT3, ENSG00000235609, TRIM38 |
| [[TNFRSF10C]] | B | TNFRSF10C activity raises TRIM5's level | lines that do not express TNFRSF10C (17) vs lines expressing it (33) | 1.52× lower at baseline in the lines without TNFRSF10C | 0.061 | ⚠ within organs, on part of the lines; also absent: LINC01426, PTGES, C1R; maybe low, not absent |
| [[TRIM38]] | B | TRIM38 activity raises TRIM5's level | lines that do not express TRIM38 (6) vs lines expressing it (44) | 2.13× lower at baseline in the lines without TRIM38 | 0.068 | ⚠ within organs, on part of the lines; also absent: SMOX, S100A13, ERAP2 |
| [[C15orf48]] | B | C15orf48 activity raises TRIM5's level | lines that do not express C15orf48 (25) vs lines expressing it (25) | 1.26× lower at baseline in the lines without C15orf48 | 0.068 | ⚠ within organs, on part of the lines; also absent: ZNF229, HMGN2P46, RHCG |
| [[OAS2]] | B | OAS2 activity strengthens TRIM5's drug response | lines that do not express OAS2 (14) vs lines expressing it (33) | the lines without OAS2 respond 0.71× as strongly (z diff +0.76); strongest at Niclosamide (olamine) 5 µM: 0.86x vs 0.60x (z diff +3.1) | 0.080 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1; target measured in part of the lines; artifact flags |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NMI]] | C | TRIM5's natural level strengthens NMI's drug response | TRIM5's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.69, reverse +0.44; direction not clear | 0.037 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[ZNFX1]] | C | TRIM5's natural level strengthens ZNFX1's drug response | TRIM5's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.44; direction not clear | 0.045 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TRIM21]] | C | TRIM5's natural level strengthens TRIM21's drug response | TRIM5's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.61; direction not clear | 0.076 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IFIT5]] | C | TRIM5's natural level strengthens IFIT5's drug response | TRIM5's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.68; direction not clear | 0.077 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TDRD7]] | C | TRIM5's natural level strengthens TDRD7's drug response | TRIM5's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.49; direction not clear | 0.091 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.832). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (48.5, 51.4); signed map (64.4, 29.1). **Vector** length 155, 52.0% of its response variance represented; |z| ≥ 3 in 1,464 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon gamma response* (hallmark, mean cos +0.62 to 25); *Antigen processing-Cross presentation* (reactome, mean cos +0.66 to 14); *Endosomal/Vacuolar pathway* (reactome, mean cos +0.65 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.3 | +12.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +10.3 | +10.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.7 | +13.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.5 | +13.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +7.4 | +5.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +6.3 | +5.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.8 | +4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +2.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +4.4 | +3.4 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -8.3 | -8.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.9 | -7.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.3 | -8.1 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -6.1 | -5.8 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -6.0 | -5.5 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -5.6 | -4.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -5.2 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:5,663,195-5,938,619 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RNF88, TRIM5alpha |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; RING finger E3 ubiquitin protein ligases |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE |
| Reactome | 3 pathways, smallest: Interferon gamma signaling; Interferon Signaling; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C035](https://www.uniprot.org/uniprotkb/Q9C035) (Tripartite motif-containing protein 5):

> Capsid-specific restriction factor that prevents infection from non-host-adapted retroviruses. Blocks viral replication early in the life cycle, after viral entry but before reverse transcription. In addition to acting as a capsid-specific restriction factor, also acts as a pattern recognition receptor that activates innate immune signaling in response to the retroviral capsid lattice. Binding to the viral capsid triggers its E3 ubiquitin ligase activity, and in concert with the heterodimeric …

**Summary**, from NCBI Gene [85363](https://www.ncbi.nlm.nih.gov/gene/85363):

> The protein encoded by this gene is a member of the tripartite motif (TRIM) family. The TRIM motif includes three zinc-binding domains, a RING, a B-box type 1 and a B-box type 2, and a coiled-coil region. The protein forms homo-oligomers via the coilel-coil region and localizes to cytoplasmic bodies. It appears to function as a E3 ubiquitin-ligase and ubiqutinates itself to regulate its subcellular localization. It may play a role in retroviral restriction. Multiple alternatively spliced …

**Accessions** — [HGNC:16276](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16276) · Entrez [85363](https://www.ncbi.nlm.nih.gov/gene/85363) · UniProt [Q9C035](https://www.uniprot.org/uniprotkb/Q9C035) · Ensembl [ENSG00000132256](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132256)

## Data

Gene col 5289: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5289); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5289, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5289]; `tensor/DDL_lfc|DDL_z.npy` [5289]; `embed/gene_vectors.npy` [5289]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5289 or target_col == 5289). Every well: [[TRIM5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
