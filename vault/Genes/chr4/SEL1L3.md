---
symbol: "SEL1L3"
type: "gene"
col: 1665
ensembl_id: "ENSG00000091490"
name: "SEL1L family member 3"
location: "4p15.2"
module: 117
arm: "+"
pooled_cpm: 59.08
n_lines_expressing: 42
n_dd_up: 21
n_dd_down: 14
n_dd_up_clean: 15
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# SEL1L3

*SEL1L family member 3* — 4p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.03× (z +15.1, q 0e+00, up in 32 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.474× (z -20.7, q 0e+00, down in 32 of 39 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.576× (z -11.8, q 1e-29, down in 25 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC7A11]] (+0.64, fdr 7e-06), [[LINC01564]] (+0.61, fdr 1e-05), [[GCLM]] (+0.61, fdr 1e-05); moves opposite to [[RBM8A]] (-0.57, fdr 1e-05), [[DOP1A]] (-0.54, fdr 3e-05), [[POLI]] (-0.54, fdr 2e-05).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[FAM149A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CCT3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1665.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.03×** | +15.1 | 0e+00 | 32/39 (HEC-1-A, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.96×** | +14.3 | 3e-44 | 34/39 (HOP62, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.93×** | +13.2 | 1e-37 | 35/40 (LoVo, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~25% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.73×** | +11.7 | 1e-29 | 30/39 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.58×** | +9.0 | 2e-17 | 27/39 (NCI-H2347, NCI-H460, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +8.1 | 5e-14 | 23/40 (HOP62, MIA PaCa-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +7.0 | 2e-10 | 20/39 (HOP62, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.72×** | +6.0 | 1e-07 | 18/35 (HEC-1-A, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.25×** | +4.8 | 9e-05 | 17/39 (A498, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.20× | +4.8 | 1e-04 | 17/40 (LoVo, A-172, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | **1.24×** | +4.6 | 2e-04 | 17/39 (HEC-1-A, NCI-H2347, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.24×** | +4.5 | 3e-04 | 20/39 (A-427, NCI-H460, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.24×** | +4.3 | 7e-04 | 15/39 (HOP62, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.23×** | +4.2 | 0.001 | 14/39 (A-172, NCI-H1573, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.21×** | +4.1 | 0.002 | 14/39 (A-172, BT-474, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.004 | 11/41 (LoVo, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.27×** | +3.7 | 0.008 | 12/41 (LoVo, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 0.5 µM |  | 1.19× | +3.6 | 0.009 | 13/40 (RKO, BT-474, …) | rises with dose |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.38×** | +3.6 | 0.011 | 13/40 (LoVo, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.19× | +3.6 | 0.011 | 16/39 (AsPC-1, hTERT-HPNE, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.17× | +3.3 | 0.025 | 15/40 (NCI-H460, Hs 766T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1665.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.474×** | -20.7 | 0e+00 | 32/39 (A498, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.465×** | -15.7 | 0e+00 | 34/40 (A498, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.576×** | -11.8 | 1e-29 | 25/40 (HT-29, SW480, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.611×** | -10.5 | 9e-24 | 26/40 (LoVo, HT-29, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.629×** | -9.9 | 5e-21 | 28/39 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.683×** | -8.1 | 4e-14 | 29/39 (A498, RKO, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.698×** | -7.7 | 1e-12 | 24/40 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.511×** | -7.4 | 8e-12 | 27/41 (LoVo, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.797×** | -6.4 | 8e-09 | 22/40 (KATO III, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.746×** | -6.2 | 2e-08 | 21/40 (A498, H4, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **0.764×** | -5.8 | 4e-07 | 15/38 (LoVo, SW48, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.928× | -5.4 | 3e-06 | 3/41 (NCI-H1792, SW 1271, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.768×** | -5.2 | 8e-06 | 20/39 (CHP-212, AN3 CA, …) | all doses, stronger at high dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **0.625×** | -5.2 | 8e-06 | 19/39 (SW48, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.839× | -3.6 | 0.012 | 14/38 (NCI-H2030, KATO III, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.816×** | -3.1 | 0.061 | 13/40 (A498, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1665. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 139 | 3 | 10 (6 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.77× (z +12.8) | [[Panobinostat (drug)]] 5 µM 0.189× (z -22.2) |
| [[SW48 (line)]] | wt | 193 | 0 | 11 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.136× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.250× (z -13.1) |
| [[SW480 (line)]] | alt | 86.6 | 2 | 9 (4 ⚠) | [[Auranofin (drug)]] 5 µM 2.07× (z +11.1) | [[Panobinostat (drug)]] 0.5 µM 0.278× (z -19.6) |
| [[LS 180 (line)]] | wt | 174 | 4 | 5 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.43× (z +11.6) | [[Panobinostat (drug)]] 5 µM 0.235× (z -18.9) |
| [[A498 (line)]] | wt | 107 | 3 (3 ⚠) | 5 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +12.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -24.5) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.514× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 123 | 4 | 4 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.82× (z +12.5) | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -20.2) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.476× (z -9.0) |
| [[HOP62 (line)]] | alt | 18.3 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.92× (z +12.3) | — |
| [[KATO III (line)]] | alt | 155 | 2 | 4 | [[Ixazomib citrate (drug)]] 5 µM 2.42× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.187× (z -20.2) |
| [[Panc 03.27 (line)]] | alt | 57.9 | 1 | 5 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.55× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.211× (z -14.6) |
| [[HT-29 (line)]] | alt | 152 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.137× (z -24.2) |
| [[NCI-H1792 (line)]] | alt | 62.4 | 1 | 3 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.06× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -14.6) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 86.1 | 2 (1 ⚠) | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.07× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -13.2) ⚠ cell-cycle shift, explains ~37% of this change |
| [[NCI-H460 (line)]] | wt | 32.1 | 1 (1 ⚠) | 3 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +10.1) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 0.5 µM 0.332× (z -10.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SW 900 (line)]] | alt | 61.3 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.10× (z +9.1) | [[Harringtonine (drug)]] 5 µM 0.317× (z -9.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SW1417 (line)]] | alt | 81.5 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.348× (z -11.8) |
| [[A-172 (line)]] | wt | 63.3 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.263× (z -13.3) ⚠ cell-cycle shift, explains ~25% of this change |
| [[COLO 205 (line)]] | alt | 64.8 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.77× (z +9.9) | — |
| [[H4 (line)]] | wt | 128 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -16.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.326× (z -8.5) |
| [[RKO (line)]] | wt | 56.1 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.161× (z -15.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[C-33 A (line)]] | alt | 22.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.168× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 82.8 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.84× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -11.8) ⚠ cell-cycle shift, explains ~37% of this change |
| [[CHP-212 (line)]] | wt | 44.0 | 0 | 2 | — | [[Decitabine (drug)]] 0.05 µM 0.0790× (z -9.4) |
| [[HS-578T (line)]] | alt | 26.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -11.7) ⚠ cell-cycle shift, explains ~37% of this change |
| [[MIA PaCa-2 (line)]] | alt | 15.1 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.52× (z +9.6) | [[Harringtonine (drug)]] 5 µM 0.112× (z -12.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H1573 (line)]] | alt | 27.7 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.23× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 55.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -14.3) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A549 (line)]] | wt | 23.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -10.9) ⚠ cell-cycle shift, explains ~37% of this change |
| [[HCT15 (line)]] | alt | 96.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -10.5) ⚠ cell-cycle shift, explains ~37% of this change |
| [[Hs 766T (line)]] | wt | 50.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -10.9) ⚠ cell-cycle shift, explains ~37% of this change |
| [[hTERT-HPNE (line)]] | wt | 31.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.195× (z -8.8) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SHP-77 (line)]] | alt | 18.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.57× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[A-427 (line)]] | wt | 58.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.03 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.47 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.5 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.19 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 8.96 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.72 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.12 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.62 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1665), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC7A11]] | +0.64 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[LINC01564]] | +0.61 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[GCLM]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[TOM1L1]] | +0.61 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[GSR]] | +0.61 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[FAM149A]] | +0.59 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[TXN]] | +0.59 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[GHITM]] | +0.59 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[IDE]] | +0.58 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[B4GALNT1]] | +0.58 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[TXNRD1]] | +0.57 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[CYP4F11]] | +0.57 | +0.59 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM8A]] | -0.57 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[DOP1A]] | -0.54 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[POLI]] | -0.54 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[C8orf58]] | -0.54 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[MTRES1]] | -0.53 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[WDPCP]] | -0.51 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[RSPRY1]] | -0.51 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[GCAT]] | -0.51 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[ZBTB48]] | -0.50 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[PEX11B]] | -0.49 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[EMC9]] | -0.49 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[HCFC2]] | -0.49 | -0.47 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM149A]] | B | FAM149A activity raises SEL1L3's level | lines that do not express FAM149A (25) vs lines expressing it (25) | 3.09× lower at baseline in the lines without FAM149A | 0.031 | ⚠ within organs, on part of the lines; also absent: SKAP1, ENSG00000286133, CSRNP3 |
| [[NMRAL2P]] | B | NMRAL2P activity raises SEL1L3's level | lines that do not express NMRAL2P (18) vs lines expressing it (32) | 1.81× lower at baseline in the lines without NMRAL2P | 0.070 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, SERPINE2, APOL1 |
| [[FRAS1]] | B | FRAS1 activity raises SEL1L3's level | lines that do not express FRAS1 (22) vs lines expressing it (28) | 2.17× lower at baseline in the lines without FRAS1 | 0.077 | ⚠ within organs, on part of the lines; also absent: ANO9, ELF3, FAAH2 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCT3]] | B | SEL1L3 activity lowers CCT3's level | lines that do not express SEL1L3 (8) vs lines expressing it (42) | 1.12× higher at baseline in the lines without SEL1L3 | 0.062 | ⚠ within organs, on part of the lines; also absent: RDH10, JDP2 |

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.573). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-10.5, 48.4); signed map (51.8, -11.2). **Vector** length 120, 32.6% of its response variance represented; |z| ≥ 3 in 1,113 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nuclear events mediated by NFE2L2* (reactome, mean cos +0.50 to 7); *KEAP1-NFE2L2 pathway* (reactome, mean cos +0.50 to 7); *NFE2L2 regulating anti-oxidant/detoxification enzymes* (reactome, mean cos +0.57 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.8 | +15.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +10.2 | +14.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +10.1 | +13.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.1 | +11.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | +6.2 | +6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +8.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.5 | +3.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.0 | +4.8 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -5.7 | -15.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -4.9 | -7.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.1 | -7.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -3.8 | -20.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -6.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.0 | -5.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -5.2 |
|  | [[HI-TOPK-032 (drug)]] 0.5 µM |  | -1.5 | -2.8 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.4 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | SEL1L family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p15.2 — chr4:25,747,433-25,863,760 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0746 |
| Matched by | ensembl_id |

UniProt [Q68CR1](https://www.uniprot.org/uniprotkb/Q68CR1) carries no function annotation.

**Summary**, from NCBI Gene [23231](https://www.ncbi.nlm.nih.gov/gene/23231):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29108](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29108) · Entrez [23231](https://www.ncbi.nlm.nih.gov/gene/23231) · UniProt [Q68CR1](https://www.uniprot.org/uniprotkb/Q68CR1) · Ensembl [ENSG00000091490](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000091490)

## Data

Gene col 1665: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1665); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1665, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1665]; `tensor/DDL_lfc|DDL_z.npy` [1665]; `embed/gene_vectors.npy` [1665]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1665 or target_col == 1665). Every well: [[SEL1L3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEL1L3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
