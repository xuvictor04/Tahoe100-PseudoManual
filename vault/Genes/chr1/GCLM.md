---
symbol: "GCLM"
type: "gene"
col: 354
ensembl_id: "ENSG00000023909"
name: "glutamate-cysteine ligase modifier subunit"
location: "1p22.1"
module: 117
arm: "+"
pooled_cpm: 77.49
n_lines_expressing: 48
n_dd_up: 38
n_dd_down: 9
n_dd_up_clean: 25
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# GCLM

*glutamate-cysteine ligase modifier subunit* — 1p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (13 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 8.96× (z +31.0, q 0e+00, up in 46 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.631× (z -6.5, q 3e-08, down in 30 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TXNRD1]] (+0.80, fdr 7e-06), [[NMRAL2P]] (+0.72, fdr 7e-06), [[ME1]] (+0.69, fdr 7e-06); moves opposite to [[PLAG1]] (-0.59, fdr 1e-05), [[TYK2]] (-0.56, fdr 1e-05), [[FUCA1]] (-0.55, fdr 2e-05).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 354.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **8.96×** | +31.0 | 0e+00 | 46/46 (LS 180, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.79×** | +18.8 | 0e+00 | 45/46 (LS 180, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.60×** | +18.1 | 0e+00 | 44/46 (LS 180, LoVo, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.47×** | +16.6 | 0e+00 | 43/46 (LS 180, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 0.5 µM |  | **2.47×** | +12.8 | 3e-35 | 43/46 (HT-29, BT-474, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.11×** | +10.6 | 4e-24 | 34/46 (NCI-H2030, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.04×** | +9.7 | 2e-20 | 35/45 (HOP62, HCT15, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.90×** | +9.1 | 7e-18 | 35/46 (A549, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.35×** | +9.0 | 2e-17 | 38/43 (LS 180, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.82×** | +7.8 | 2e-13 | 32/43 (NCI-H1792, A549, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +7.2 | 2e-11 | 29/42 (NCI-H1792, A549, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.65×** | +7.1 | 6e-11 | 32/46 (HT-29, NCI-H1792, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.99×** | +6.9 | 2e-10 | 34/47 (LS 180, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Infigratinib (drug)]] 5 µM |  | **2.05×** | +5.3 | 5e-06 | 33/46 (LS 180, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.44×** | +5.1 | 1e-05 | 26/46 (NCI-H1792, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.29×** | +5.1 | 2e-05 | 33/46 (LoVo, CFPAC-1, …) | rises with dose | position effect removed |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.42×** | +4.9 | 3e-05 | 24/46 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +4.7 | 9e-05 | 24/46 (NCI-H23, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.35×** | +4.2 | 8e-04 | 25/46 (NCI-H460, LOX-IMVI, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +3.6 | 0.008 | 17/46 (A549, NCI-H2030, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.013 | 19/46 (LoVo, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 354.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.631×** | -6.5 | 3e-08 | 30/46 (MIA PaCa-2, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.640×** | -6.3 | 6e-08 | 33/46 (RKO, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.667×** | -5.8 | 2e-06 | 27/46 (MIA PaCa-2, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.768×** | -5.3 | 1e-05 | 27/46 (RKO, KATO III, …) | all doses, flat | low cells (technical?) |
| [[Ciclopirox (drug)]] 5 µM |  | **0.778×** | -5.1 | 5e-05 | 29/46 (SNU-1, NCI-H23, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM |  | **0.717×** | -4.7 | 2e-04 | 30/47 (RKO, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.812×** | -4.2 | 0.002 | 21/46 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.765×** | -3.8 | 0.010 | 22/46 (KATO III, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.627×** | -3.5 | 0.033 | 17/47 (SNU-1, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.808× | -3.0 | 0.13 | 16/46 (LoVo, J82, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 354. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 439 | 1 | 19 (4 ⚠) | [[Auranofin (drug)]] 5 µM 2.62× (z +9.5) | [[Adagrasib (drug)]] 0.05 µM 0.415× (z -30.9) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -20.6) |
| [[NCI-H1792 (line)]] | alt | 40.8 | 12 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +17.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.97× (z +14.1) | — |
| [[KATO III (line)]] | alt | 76.5 | 6 | 5 (1 ⚠) | [[Auranofin (drug)]] 5 µM 8.56× (z +19.6) | [[Panobinostat (drug)]] 5 µM 0.304× (z -10.8) |
| [[HOP62 (line)]] | alt | 31.4 | 8 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 13.4× (z +19.5) | — |
| [[HT-29 (line)]] | alt | 99.0 | 7 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 13.0× (z +20.8) | — |
| [[LoVo (line)]] | wt | 72.8 | 5 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 15.8× (z +23.8) | [[Selinexor (drug)]] 5 µM 0.437× (z -10.2) ⚠ cell-cycle shift, explains ~33% of this change |
| [[CFPAC-1 (line)]] | alt | 27.4 | 6 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 21.2× (z +21.7) | — |
| [[HCT15 (line)]] | alt | 50.1 | 6 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 20.2× (z +19.6) | — |
| [[HEC-1-A (line)]] | alt | 56.8 | 5 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 11.5× (z +20.0) | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 52.0 | 6 | 0 | [[Auranofin (drug)]] 5 µM 12.4× (z +18.5) | — |
| [[SNU-423 (line)]] | alt | 44.5 | 6 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 8.30× (z +16.7) | — |
| [[SW480 (line)]] | alt | 48.5 | 6 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 11.0× (z +24.3) | — |
| [[A549 (line)]] | wt | 59.1 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.11× (z +14.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 4.60× (z +11.6) | — |
| [[LS 180 (line)]] | wt | 46.9 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 22.1× (z +24.8) | — |
| [[NCI-H23 (line)]] | alt | 98.6 | 4 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.96× (z +13.3) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 48.7 | 5 | 0 | [[Auranofin (drug)]] 5 µM 10.3× (z +24.2) | — |
| [[PANC-1 (line)]] | alt | 79.7 | 3 | 2 | [[Auranofin (drug)]] 5 µM 5.96× (z +19.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -10.5) |
| [[A-172 (line)]] | wt | 37.0 | 4 | 0 | [[Auranofin (drug)]] 5 µM 12.5× (z +21.0) | — |
| [[A498 (line)]] | wt | 162 | 3 (2 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.10× (z +10.3) | [[Selinexor (drug)]] 5 µM 0.369× (z -10.2) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HepG2_C3A (line)]] | wt | 53.2 | 4 | 0 | [[Auranofin (drug)]] 5 µM 17.5× (z +18.6) | — |
| [[hTERT-HPNE (line)]] | wt | 43.3 | 4 | 0 | [[Auranofin (drug)]] 5 µM 10.1× (z +13.8) | — |
| [[NCI-H460 (line)]] | wt | 96.1 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 3.60× (z +10.7) | — |
| [[Panc 03.27 (line)]] | alt | 40.1 | 4 | 0 | [[Auranofin (drug)]] 5 µM 13.6× (z +19.5) | — |
| [[RKO (line)]] | wt | 83.0 | 2 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 8.03× (z +15.2) | [[Selinexor (drug)]] 5 µM 0.265× (z -13.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[RPMI-7951 (line)]] | alt | 56.6 | 4 | 0 | [[Auranofin (drug)]] 5 µM 10.7× (z +16.0) | — |
| [[SNU-1 (line)]] | wt | 177 | 1 | 3 (2 ⚠) | [[Auranofin (drug)]] 5 µM 4.09× (z +9.9) | [[Harringtonine (drug)]] 5 µM 0.207× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ciclopirox (drug)]] 5 µM 0.392× (z -9.3) |
| [[SW1417 (line)]] | alt | 46.5 | 3 | 1 | [[Auranofin (drug)]] 5 µM 11.2× (z +19.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -9.6) |
| [[BT-474 (line)]] | alt | 20.7 | 3 | 0 | [[Auranofin (drug)]] 5 µM 15.4× (z +13.7) | — |
| [[COLO 205 (line)]] | alt | 31.1 | 3 | 0 | [[Auranofin (drug)]] 5 µM 17.0× (z +13.7) | — |
| [[Hs 766T (line)]] | wt | 85.9 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 8.78× (z +17.0) | — |
| [[HS-578T (line)]] | alt | 104 | 3 | 0 | [[Auranofin (drug)]] 5 µM 4.34× (z +13.0) | — |
| [[NCI-H1573 (line)]] | alt | 130 | 1 | 2 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 4.15× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.288× (z -8.5) |
| [[SW48 (line)]] | wt | 71.9 | 3 | 0 | [[Auranofin (drug)]] 5 µM 9.14× (z +15.9) | — |
| [[A-427 (line)]] | wt | 53.9 | 1 | 1 | [[Auranofin (drug)]] 5 µM 5.09× (z +15.3) | [[Panobinostat (drug)]] 5 µM 0.397× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 21.2 | 1 | 1 | [[Auranofin (drug)]] 5 µM 26.9× (z +18.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -10.0) |
| [[C-33 A (line)]] | alt | 66.2 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 7.89× (z +13.8) | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 61.2 | 2 | 0 | [[Auranofin (drug)]] 5 µM 5.40× (z +9.3) | — |
| [[J82 (line)]] | alt | 80.0 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.74× (z +14.3) | — |
| [[SK-MEL-2 (line)]] | alt | 54.4 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.02× (z +13.1) | — |
| [[AN3 CA (line)]] | alt | 58.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 11.9× (z +11.9) | — |
| [[NCI-H2030 (line)]] | alt | 124 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.84× (z +14.8) | — |
| [[SHP-77 (line)]] | alt | 50.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.05× (z +10.8) | — |
| [[SW 1271 (line)]] | alt | 42.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 18.1× (z +9.1) | — |
| [[SW 900 (line)]] | alt | 59.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.48× (z +13.7) | — |
| [[C32 (line)]] | wt | 18.1 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 17.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 354), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNRD1]] | +0.80 | +0.79 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_REACTIVE_OXYGEN_SPECIES_PATHWAY; STRING 795 |
| [[NMRAL2P]] | +0.72 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[ME1]] | +0.69 | +0.66 / +0.65 | both halves | 7e-06 | pathway: Cellular response to chemical stress; STRING 538 |
| [[VEGFD]] | +0.68 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[SLC7A11]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_HEME_METABOLISM; STRING 689 |
| [[PIR]] | +0.67 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[PSMD11]] | +0.67 | +0.67 / +0.63 | both halves | 7e-06 | pathway: Cellular response to chemical stress |
| [[PSMD1]] | +0.66 | +0.62 / +0.69 | both halves | 7e-06 | pathway: Cellular response to chemical stress |
| [[CYP4F11]] | +0.65 | +0.63 / +0.67 | both halves | 7e-06 | pathway: Biological oxidations |
| [[IDE]] | +0.64 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[EID3]] | +0.64 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[NMRAL2P-1]] | +0.63 | +0.58 / +0.64 | both halves | 8e-06 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLAG1]] | -0.59 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[TYK2]] | -0.56 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[FUCA1]] | -0.55 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[PPDPF]] | -0.55 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[PAIP2B]] | -0.55 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[MMUT]] | -0.54 | -0.52 / -0.49 | both halves | 2e-05 | pathway: Diseases of metabolism |
| [[MHENCR]] | -0.54 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[NDUFA2]] | -0.53 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[KLHL28]] | -0.52 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[TMA7]] | -0.52 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[PER1]] | -0.51 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[KATNA1]] | -0.50 | -0.40 / -0.52 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises GCLM's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.795). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-8.7, 48.2); signed map (51.4, -10.4). **Vector** length 130, 40.1% of its response variance represented; |z| ≥ 3 in 1,480 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +13.8 | +31.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +12.8 | +18.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +12.2 | +18.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +11.9 | +16.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +6.0 | +9.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.7 | +6.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.2 | +3.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.2 | +5.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -5.9 | -5.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -4.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.6 | -3.5 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -4.4 | -6.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | -3.8 | +0.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.9 | -1.5 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -2.7 | -2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.5 | -0.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -2.4 | -1.5 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | glutamate-cysteine ligase modifier subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.1 — chr1:93,885,199-93,909,456 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously GLCLR |
| Gene groups (HGNC) | Glutamate-cysteine ligase subunits |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY, BILE_ACID_METABOLISM, HEME_METABOLISM |
| Reactome | 12 pathways, smallest: Glutathione synthesis and recycling; NFE2L2 regulating anti-oxidant/detoxification enzymes; Metabolic disorders of biological oxidation enzymes |
| Matched by | ensembl_id |

UniProt [P48507](https://www.uniprot.org/uniprotkb/P48507) carries no function annotation.

**Summary**, from NCBI Gene [2730](https://www.ncbi.nlm.nih.gov/gene/2730):

> Glutamate-cysteine ligase, also known as gamma-glutamylcysteine synthetase, is the first rate limiting enzyme of glutathione synthesis. The enzyme consists of two subunits, a heavy catalytic subunit and a light regulatory subunit. Gamma glutamylcysteine synthetase deficiency has been implicated in some forms of hemolytic anemia. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Apr 2015]

**Accessions** — [HGNC:4312](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4312) · Entrez [2730](https://www.ncbi.nlm.nih.gov/gene/2730) · UniProt [P48507](https://www.uniprot.org/uniprotkb/P48507) · Ensembl [ENSG00000023909](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000023909)

## Data

Gene col 354: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 354); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 354, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 354]; `tensor/DDL_lfc|DDL_z.npy` [354]; `embed/gene_vectors.npy` [354]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 354 or target_col == 354). Every well: [[GCLM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GCLM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
